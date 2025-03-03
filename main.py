from contextlib import asynccontextmanager
from database import connect_db, close_db, database
from entities.serviceOrder import ServiceOrder, ServiceOrderPart, ServiceOrderState
from entities.vehicle import Vehicle
from entities.part import Part
from models.serviceOrderModel import ServiceOrderModel
from models.vehicleModel import VehicleModel
from models.partModel import PartModel
from peewee import ModelSelect
from typing import List, Optional
from datetime import date

from fastapi import FastAPI, Depends, HTTPException

app = FastAPI()


def get_db():
    """
    Dependencia para conectar y desconectar la base de datos.
    """
    try:
        connect_db()
        yield
    finally:
        close_db()


def convert_date_to_str(date_obj: date) -> Optional[str]:
    return date_obj.isoformat() if date_obj else None


@asynccontextmanager
async def lifespan(app: FastAPI):
    """
    Context manager para el ciclo de vida de la aplicación.
    Conecta a la base de datos y crea las tablas necesarias al iniciar,
    y cierra la conexión a la base de datos al finalizar.
    """
    # Conectar a la base de datos y crear tablas
    database.connect()
    database.create_tables([Vehicle, ServiceOrder, ServiceOrderPart, Part], safe=True)
    yield
    # Cerrar la conexión a la base de datos
    database.close()


app.router.lifespan_context = lifespan


@app.post("/vehicles", response_model=VehicleModel, dependencies=[Depends(get_db)])
def create_vehicle(vehicle: VehicleModel):
    """
    Crea un nuevo vehículo en la base de datos.

    Args:
        vehicle (VehicleModel): Datos del vehículo a crear.

    Returns:
        VehicleModel: El vehículo creado.
    """
    try:
        vehicle_data = vehicle.model_dump()
        new_vehicle = Vehicle.create(**vehicle_data)
        return new_vehicle
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))


@app.get("/vehicles", response_model=List[VehicleModel], dependencies=[Depends(get_db)])
def read_all_vehicles():
    """
    Obtiene todos los vehículos de la base de datos.

    Returns:
        List[VehicleModel]: Lista de vehículos.
    """
    try:
        vehicles: ModelSelect = Vehicle.select()
        return list(vehicles)
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))


@app.post(
    "/service_orders", response_model=ServiceOrderModel, dependencies=[Depends(get_db)]
)
def create_service_order(order: ServiceOrderModel):
    """
    Crea una nueva orden de servicio en la base de datos.

    Args:
        order (ServiceOrderModel): Datos de la orden de servicio a crear.

    Returns:
        ServiceOrderModel: La orden de servicio creada.
    """
    try:
        # Crear la orden de servicio en la base de datos
        new_order = ServiceOrder.create(
            vehicle=order.vehicle_id,
            current_mileage=order.current_mileage,
            maintenance_date=order.maintenance_date,
            maintenance_type=order.maintenance_type,
            maintenance_cost=order.maintenance_cost,
            service_provider=order.service_provider,
            recommended_next_maintenance=order.recommended_next_maintenance,
            notes=order.notes,
            repair_history=order.repair_history,
            vehicle_condition=order.vehicle_condition,
            attached_documents=order.attached_documents,
            state=order.state.value,
            operation_description=order.operation_description,
            start_date=order.start_date,
            end_date=order.end_date,
        )
        part_ids = []
        # Añadir las partes mecánicas involucradas en la orden de servicio
        for part_id in order.parts:
            ServiceOrderPart.create(serviceorder=new_order.id, part=part_id)
            part_ids.append(part_id)

        response_data = {
            **new_order.__data__,
            "vehicle_id": order.vehicle_id,
            "parts": part_ids,
        }
        return ServiceOrderModel(**response_data)
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))


@app.put(
    "/service_orders/{order_id}/state",
    response_model=ServiceOrderModel,
    dependencies=[Depends(get_db)],
)
def update_service_order_state(order_id: int, state: ServiceOrderState):
    """
    Actualiza el estado de una orden de servicio.

    Args:
        order_id (int): ID de la orden de servicio.
        state (ServiceOrderState): Nuevo estado de la orden de servicio.

    Returns:
        ServiceOrderModel: La orden de servicio actualizada.
    """
    try:
        order = ServiceOrder.get_by_id(order_id)
        if state not in ServiceOrderState:
            raise HTTPException(status_code=400, detail="Invalid state")
        order.state = state.value
        order.save()
        return order
    except ServiceOrder.DoesNotExist:
        raise HTTPException(status_code=404, detail="Service order not found")
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))


@app.get(
    "/vehicles/{vehicle_id}/service_orders",
    response_model=List[ServiceOrderModel],
    dependencies=[Depends(get_db)],
)
def get_service_orders_by_vehicle(vehicle_id: int):
    """
    Obtiene las órdenes de servicio de un vehículo específico.

    Args:
        vehicle_id (int): ID del vehículo.

    Returns:
        List[ServiceOrderModel]: Lista de órdenes de servicio del vehículo.
    """
    try:
        orders: ModelSelect = ServiceOrder.select().where(
            ServiceOrder.vehicle == vehicle_id
        )
        service_order_list = []
        for order in orders:
            service_order_list.append(
                ServiceOrderModel(
                    vehicle_id=order.vehicle.id,
                    current_mileage=order.current_mileage,
                    maintenance_date=convert_date_to_str(order.maintenance_date),
                    maintenance_type=order.maintenance_type,
                    maintenance_cost=order.maintenance_cost,
                    service_provider=order.service_provider,
                    recommended_next_maintenance=convert_date_to_str(
                        order.recommended_next_maintenance
                    ),
                    notes=order.notes,
                    repair_history=order.repair_history,
                    vehicle_condition=order.vehicle_condition,
                    attached_documents=order.attached_documents,
                    state=order.state,
                    operation_description=order.operation_description,
                    parts=[part.id for part in order.parts],
                    start_date=convert_date_to_str(order.start_date),
                    end_date=convert_date_to_str(order.end_date),
                )
            )
        return service_order_list
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))


@app.post("/parts", response_model=PartModel, dependencies=[Depends(get_db)])
def create_part(part: PartModel):
    """
    Crea una nueva parte mecánica en la base de datos.

    Args:
        part (PartModel): Datos de la parte a crear.

    Returns:
        PartModel: La parte creada.
    """
    try:
        part_data = part.model_dump()
        new_part = Part.create(**part_data)
        return new_part
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

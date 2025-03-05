# ServiceOrders_API

## Descripción

ServiceOrders_API es una API diseñada para gestionar órdenes de servicio. Este proyecto proporciona una solución completa para el manejo de solicitudes de servicio, incluyendo creación, actualización y seguimiento de órdenes.

## Requisitos

Antes de comenzar, asegúrate de tener instalados los siguientes requisitos:

- [Python](https://www.python.org/) (versión 3.13.2 o superior)
- [pip](https://pip.pypa.io/en/stable/)

## Instalación

Sigue estos pasos para instalar y ejecutar el proyecto en tu máquina local:

1. Clona el repositorio:
    ```bash
    git clone https://github.com/GustavoRojasJDL/ServiceOrders_API.git
    cd ServiceOrders_API
    ```

2. Crea un entorno virtual:
    ```bash
    python -m venv env
    source env/bin/activate  # En Windows usa `env\Scripts\activate`
    ```

3. Instala las dependencias:
    ```bash
    pip install -r requirements.txt
    ```

4. Inicia el servidor:
    ```bash
    fastapi dev main.py
    ```

## Uso

Antes de enviar órdenes de servicio, asegúrate de agregar los vehículos y las partes mecánicas necesarias. Aquí tienes algunos ejemplos de cómo hacerlo:

- **Agregar un nuevo vehículo**
    ```bash
    POST /vehicles
    {
      "brand": "Toyota",
      "model": "Corolla",
      "year": 2020,
      "plate": "ABC-1234",
      "vin": "1HGCM82633A123456",
      "purchase_date": "2020-01-15",
      "warranty": "3 años",
      "fuel_type": "Gasolina"
    }
    ```

    - **Propiedades del vehículo (`VehicleModel`)**:
        - `brand`: Marca del vehículo (ej. "Toyota")
        - `model`: Modelo del vehículo (ej. "Corolla")
        - `year`: Año del vehículo (ej. 2020)
        - `plate`: Placa del vehículo (ej. "ABC-1234")
        - `vin`: Número de identificación del vehículo (opcional) (ej. "1HGCM82633A123456")
        - `purchase_date`: Fecha de compra del vehículo (opcional) (ej. "2020-01-15")
        - `warranty`: Garantía del vehículo (opcional) (ej. "3 años")
        - `fuel_type`: Tipo de combustible del vehículo (opcional) (ej. "Gasolina")

- **Agregar una nueva parte mecánica**
    ```bash
    POST /parts
    {
      "name": "Filtro de aire",
      "description": "Filtro de aire para motor"
    }
    ```
    
    - **Propiedades de la parte mecánica (`PartModel`)**:
        - `name`: Nombre de la parte mecánica (ej. "Filtro de aire")
        - `description`: Descripción de la parte mecánica (ej. "Filtro de aire para 

- **Crear una nueva orden de servicio**
    ```bash
    POST /orders
    {
      "vehicle_id": 1,
      "current_mileage": 15000,
      "maintenance_date": "2023-03-15",
      "maintenance_type": "Mantenimiento",
      "maintenance_cost": 200.0,
      "service_provider": "Taller Mecánico ABC",
      "recommended_next_maintenance": "2023-09-15",
      "notes": "Cambio de aceite y filtro",
      "repair_history": "Reemplazo de frenos en 2022",
      "vehicle_condition": "Buena",
      "attached_documents": "factura_123.pdf",
      "state": "CREATED",
      "operation_description": "Mantenimiento general",
      "parts": [1, 2],
      "start_date": "2023-03-15",
      "end_date": "2023-03-15"
    }
    ```

    - **Propiedades de la orden de servicio (`ServiceOrderModel`)**:
        - `vehicle_id`: ID del vehículo asociado (ej. 1)
        - `current_mileage`: Kilometraje actual del vehículo (opcional) (ej. 15000)
        - `maintenance_date`: Fecha de mantenimiento (opcional) (ej. "2023-03-15")
        - `maintenance_type`: Tipo de mantenimiento (opcional) (ej. "Mantenimiento")
        - `maintenance_cost`: Costo del mantenimiento (opcional) (ej. 200.0)
        - `service_provider`: Proveedor del servicio (opcional) (ej. "Taller Mecánico ABC")
        - `recommended_next_maintenance`: Fecha recomendada para el próximo mantenimiento (opcional) (ej. "2023-09-15")
        - `notes`: Notas adicionales (opcional) (ej. "Cambio de aceite y filtro")
        - `repair_history`: Historial de reparaciones (opcional) (ej. "Reemplazo de frenos en 2022")
        - `vehicle_condition`: Condición del vehículo (opcional) (ej. "Buena")
        - `attached_documents`: Documentos adjuntos (opcional) (ej. "factura_123.pdf")
        - `state`: Estado de la orden de servicio (opcional) (ej. "CREATED")
        - `operation_description`: Descripción de la operación (ej. "Mantenimiento general")
        - `parts`: Lista de IDs de las partes mecánicas utilizadas (opcional) (ej. [1, 2])
        - `start_date`: Fecha de inicio del servicio (opcional) (ej. "2023-03-15")
        - `end_date`: Fecha de finalización del servicio (opcional) (ej. "2023-03-15")

- **Obtener todas las órdenes de servicio**
    ```bash
    GET /orders
    ```

- **Obtener órdenes de servicio por vehículo**
    ```bash
    GET /vehicles/{vehicle_id}/orders
    ```

## Licencia

Este proyecto está licenciado bajo los términos de la licencia MIT. Consulta el archivo `LICENSE` para más detalles.

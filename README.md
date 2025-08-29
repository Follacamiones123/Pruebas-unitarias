# Proyecto Backend - Pruebas Unitarias (SENA - ADSO)

## Descripción del Proyecto

Este repositorio contiene el código backend para un sistema de gestión de un modelo de negocio simple (usuarios, productos, pedidos). El objetivo principal de este proyecto es demostrar la implementación de **pruebas unitarias** en Python utilizando el módulo `unittest` para garantizar la calidad y el correcto funcionamiento del código.

## Tecnologías Utilizadas

* **Lenguaje:** Python 3
* **Framework de Pruebas:** `unittest` (módulo estándar de Python)
* **Base de Datos (Ejemplo):** SQLite (compatible con el script SQL proporcionado)

## Instrucciones de Despliegue e Instalación

Para configurar el proyecto en una máquina local, sigue estos pasos:

1.  **Clonar el repositorio:**
    ```bash
    git clone <URL_DE_TU_REPOSITORIO_EN_GITHUB>
    cd <NOMBRE_DEL_PROYECTO>
    ```

2.  **(Opcional) Crear un entorno virtual:** Se recomienda para aislar las dependencias del proyecto.
    ```bash
    python -m venv venv
    source venv/bin/activate  # En Windows: venv\Scripts\activate
    ```

3.  **Importar la base de datos:** Si estás usando SQLite, puedes crear e importar la base de datos con el siguiente comando:
    ```bash
    sqlite3 mi_base_de_datos.db < database.sql
    ```
    Esto creará un archivo `mi_base_de_datos.db` con la estructura y los datos de ejemplo.

## Instrucciones de Ejecución del Proyecto

Actualmente, el proyecto se centra en las clases del modelo y sus pruebas. No hay un servidor o aplicación principal para ejecutar. El código se puede explorar y probar a través de las pruebas unitarias.

## Instrucciones de Ejecución de las Pruebas Unitarias

Para verificar que todo el código funciona correctamente, puedes ejecutar las pruebas unitarias. Asegúrate de estar en la carpeta raíz del proyecto.

Puedes ejecutar cada archivo de prueba de forma individual con los siguientes comandos:

```bash
python test_usuario.py
python test_categoria.py
python test_producto.py
python test_pedido.py
python test_detalle_pedido.py
```


# Proyecto Backend - Pruebas Unitarias (SENA - ADSO)

## Descripción del Proyecto
Este repositorio contiene el código backend para un sistema simple y demuestra la implementación de **pruebas unitarias** en Python con `unittest` para 5 clases del modelo de negocio.

## Estructura de Archivos
El proyecto está organizado con cada clase en su propio archivo (`.py`) y sus pruebas en un archivo `test_` correspondiente.

## Instrucciones de Despliegue e Instalación
1.  **Clonar el repositorio:**
    ```bash
    git clone <URL_DE_TU_REPOSITORIO>
    cd <NOMBRE_DEL_PROYECTO>
    ```
2.  **(Opcional) Crear un entorno virtual:**
    ```bash
    python -m venv venv
    source venv/bin/activate
    ```
3.  **Importar la base de datos (ejemplo con SQLite):**
    ```bash
    sqlite3 mi_base_de_datos.db < database.sql
    ```

## Ejecución de las Pruebas Unitarias
Para verificar el correcto funcionamiento del código, ejecuta cada archivo de prueba de forma individual. Cada `OK` significa que las pruebas de esa clase pasaron.

```bash
python test_usuario.py
python test_categoria.py
python test_producto.py
python test_pedido.py
python test_detalle_pedido.py
```
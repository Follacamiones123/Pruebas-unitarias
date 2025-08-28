# Proyecto Backend - Pruebas Unitarias (SENA - ADSO)

## Descripción del Proyecto
Este repositorio contiene el código backend para un sistema simple y demuestra la implementación de **pruebas unitarias** en Python con `unittest` para 5 clases del modelo de negocio.

## Estructura de Archivos
El proyecto está organizado con cada clase en su propio archivo (`.py`) y sus pruebas en un archivo `test_` correspondiente.

## Instrucciones de Despliegue e Instalación
1.  **Clonar el repositorio:**
    ```bash
    git clone https://github.com/Kevin-Florez/construsys-pruebas-unitarias.git
    cd construsys-pruebas-unitarias
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

Puedes verificar el correcto funcionamiento del código ejecutando cada archivo de prueba de forma individual:

```bash
python test_usuario.py
python test_categoria.py
python test_producto.py
python test_pedido.py
python test_detalle_pedido.py
```


## 🚀 Automatización con GitHub Actions

Este repositorio incluye un flujo de trabajo de Integración Continua (CI) utilizando GitHub Actions.

### Configuración y Despliegue Automático

El flujo de trabajo se encuentra definido en el archivo `.github/workflows/python-tests.yml` y realiza las siguientes acciones de manera automática:

1.  **Disparadores (Triggers)**: La automatización se activa automáticamente cada vez que se realiza un `push` o un `pull request` a la rama `main`.
2.  **Entorno de Ejecución**: Se configura un entorno virtual con Ubuntu y Python 3.10.
3.  **Ejecución de Pruebas**: Se ejecutan todas las pruebas unitarias del proyecto de forma automática utilizando el comando `python -m unittest discover`.

Esto asegura que cualquier cambio nuevo subido al repositorio sea verificado y no rompa la funcionalidad existente, garantizando la calidad y estabilidad del código. Los resultados de cada ejecución se pueden ver en la pestaña **"Actions"** del repositorio.
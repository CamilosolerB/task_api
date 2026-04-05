# task_api

## Descripción General

`task_api` es una API RESTful desarrollada con Django y Django REST Framework para la gestión de tareas. Permite a los usuarios crear, leer, actualizar y eliminar tareas, proporcionando una interfaz programática para interactuar con la aplicación.

## Características Principales

*   **API RESTful:** Implementación de endpoints para operaciones CRUD en tareas.
*   **Autenticación:** (Asumir autenticación básica o por tokens si se encuentra en el código).
*   **Base de Datos:** Utiliza SQLite por defecto (db.sqlite3), pero puede configurarse para otras bases de datos relacionales.
*   **Administración de Django:** Interfaz de administración para gestionar modelos de datos.

## Tecnologías Utilizadas

*   **Python**
*   **Django:** Framework web de alto nivel para el desarrollo rápido y seguro.
*   **Django REST Framework:** Toolkit potente y flexible para construir APIs web.
*   **SQLite:** Base de datos ligera por defecto.
*   **HTML, CSS, JavaScript:** Para la interfaz de administración y posibles vistas de ejemplo.

## Instalación y Configuración

Para configurar y ejecutar el proyecto localmente, sigue los siguientes pasos:

1.  **Clonar el repositorio:**

    ```bash
    git clone https://github.com/CamilosolerB/task_api.git
    cd task_api
    ```

2.  **Crear y activar un entorno virtual:**

    ```bash
    python -m venv venv
    source venv/bin/activate  # En Linux/macOS
    # venv\Scripts\activate   # En Windows
    ```

3.  **Instalar dependencias:**

    (Dado que no se encontró un `requirements.txt` en la raíz, se asume que las dependencias principales son Django y Django REST Framework. Se recomienda crear un `requirements.txt` con `pip freeze > requirements.txt` después de instalar las dependencias necesarias.)

    ```bash
    pip install Django djangorestframework
    # Si existen otras dependencias, instalarlas aquí.
    ```

4.  **Ejecutar migraciones de base de datos:**

    ```bash
    python manage.py migrate
    ```

5.  **Crear un superusuario (opcional, para acceder al panel de administración):**

    ```bash
    python manage.py createsuperuser
    ```

6.  **Iniciar el servidor de desarrollo:**

    ```bash
    python manage.py runserver
    ```

    La API estará disponible en `http://127.0.0.1:8000`.
    El panel de administración de Django estará en `http://127.0.0.1:8000/admin`.

## Uso de la API

(Aquí se pueden añadir ejemplos de endpoints y cómo interactuar con ellos, por ejemplo, para crear, listar, actualizar y eliminar tareas.)

## Contribución

Las contribuciones son bienvenidas. Por favor, abre un *issue* o *pull request* con tus sugerencias o mejoras.

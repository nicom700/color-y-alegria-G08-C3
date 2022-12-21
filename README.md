# Color y alegria

Proyecto final del Informatorio 2022 (Grupo 08 - Comisión 3) - para la ONG Color y alegria

## Instalación 📋

- Configurar variables de entorno

    > Copiar el archivo .env.example y renombrarlo a .env

    ```
    DATABASE_NAME=nombre_de_la_DB
    DATABASE_USER=usuario_de_la_DB
    DATABASE_PASSWORD=contraseña_de_la_DB
    DATABASE_HOST=host_de_la_DB

    LANGUAGE_CODE=idioma    #por defecto en-us
    TIME_ZONE=zona_horaria  #por defecto UTC
    ```

- Instalar las dependendencias del proyecto

    ```
    pip install -r requirements.txt
    ```
- Instalar paquetes (node)

    ```
    npm install
    ```
- Watch tailwind (solo en desarrollo)

    ```
    npx tailwindcss -i ./static/src/input.css -o ./static/src/output.css --watch
    ```

## Tecnologías 🛠️

* [Django] Framework web
* [SQL Server] Base de datos
* [Tailwind] Frontend

---
Informatorio 2022 (Grupo 08 - Comisión 3)
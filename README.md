# Comandos para ejecutar el proyecto

En la carpeta de PeliculasReseñas

```
python -m venv .env

.env\Scripts\activate

pip install django

django-admin startproject movies_project
```

Hacer cd en la siguienta ruta

```
cd movies_project

python manage.py startapp cinema

python manage.py makemigrations

python manage.py migrate

pip install 'strawberry-graphql[debug-server]'

pip install strawberry-graphql-django
```

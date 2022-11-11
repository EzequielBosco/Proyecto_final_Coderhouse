# Proyecto Final Coderhouse Python
Este es el proyecto final de Coderhouse, se trata de un sistema web realizado en python con django
## Lista de integrantes 
Comisión 44065
- Ezequiel Bosco
- Esteban Santillan

# Proyecto Codeo Blog
Página web de un blog que habla sobre Tecnologias de Programacion, donde cualquier usuario puede:
- Registrar una cuenta en registro de la barra de navegación
- Iniciar sesión
- Modificar el usuario
- Borra el usuario
- Ver los blogs publicados
- Crear un blog
- Editar un blog
- Borrar un blog
- Dejar un mensaje de contacto
- Ver más información sobre los desarrolladores en Acerca de nosotros de la barra de navegación

# Tecnología usada
- Pyhon
- Django
- Html
- Css
- Javascript
- Bootstrap

# Requisitos para correr el proyecto
## Tener instalado:
```python
python version 3.10.8 
django version 4.0.3
pillow version 9.3.6
whitenoise version 6.2.0
```
## Correr los comandos: 
Para realizar las migraciones,este proyecto usa SQLite3
```python
> python manage.py makemigrations
> python manage.py migrate

```

Para juntar los estaticos (imagenes)
```python
> python manage.py collectstatic

```

## Para ir al blog se necesita:
- Correr test server en terminal
```python
> python manage.py runserver
```
- Ir a localhost:8000/ en el navegador
Ya vas a tener acceso al inicio del blog y a sus utilidades antes mencionadas.

# 3ra Pre-entrega

## Instrucciones instalar proyecto en local
+ Crea una carpeta contenedora madre
+ Abre la consola y ubicate en la carpeta madre
+ Clona este proyecto en la carpeta madre
+ Entra en la carpeta que acabas de clonar
+ Para instalar las dependencias corre este comando:

```
pip install -r requirements.txt
```

## Instrucciones para entrar al panel aministrativo de Django
+ En consola, crear un superuser:
```
python manage.py createsuperuser
```
+ Acceder con user y password via:
```
127.0.0.1:8000/admin
```

# Superusuario de pruebas
username:admin
contraseña:password

# Usuarios normales
??

# Instrucciones para probar el funcionamiento
+ Abrir la consola y ubicarse en la carpeta ¨tercera_entrega¨. Luego, correr el comando
```
python manage.py runserver
```
+ Abrir enlace generado
```
http://127.0.0.1:8000/
```
+ Tocar 'Genre', 'Movies' o 'Series'. Dentro de cada apartado, se encontrarán un formulario de busqueda y dos botones con distintos accesos.
+ Pulsar sobre 'Añadir género', 'Añadir película' o 'Añadir serie' según corresponda.
+ Completar la información solicitada por el formulario y enviar. Repetir este paso cuantas veces se desee.
+ Buscar un género, serie o película.
+ Pulsar 'Ver todos'.
+ Repetir el procedimiento con los models restantes


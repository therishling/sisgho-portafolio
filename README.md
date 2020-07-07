# SISGHO PORTAFOLIO


Proyecto de portafolio de titulo, el cual gestiona una hostal y todos sus servicios.

## Desarrollo

  - Sistema Escritorio en C# Para la parte administrativa
  - Sistema WEB en Django 3.0.6, para clientes, empleados y proveedores.


## Configuracion
Para el correcto funcionamiento del sistema web, se debe crear una base de datos oracle y configurar tanto el connectionstring y el settings.py, ademas se deben instalar las librerias usadas en el sistema web ejecutando el siguiente comando:

> pip install -r requirements.txt

Se debe ademas, configurar el correo electronico en settings.py

```
EMAIL_USE_TLS = True
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 25
EMAIL_HOST_USER = 'TU CORREO AQUI'
EMAIL_HOST_PASSWORD = 'TU CONTRASEÑA'
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
```

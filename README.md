# challenge-traffic-ticket

# Image Docker 
docker pull almagro/challenge-traffic-ticket

## Configuración del entorno virtual (Opción 1)

Para trabajar en un entorno virtual y aislar las dependencias del proyecto, sigue estos pasos:

1. **Instalar el entorno virtual:**

```bash
pip install virtualenv
```

2. **Crear y activar el entorno virtual:**

```bash
virtualenv venv 
source venv/bin/activate 
```

3. **Instalar las dependencias del proyecto:**

```bash
pip install -r requirements.txt
```

4. **Aplicar las migraciones de la base de datos:**

```bash
cd trafficTicket && python manage.py migrate
```

5. **Crear un superusuario (opcional):**

```bash
python manage.py createsuperuser
```
```bash
python manage.py runserver
```

# se procede a cargar un usuario (Person)
http://localhost:8000/admin/traffic_violations/person/add/

# se realiza la carga de vehiculos 
http://localhost:8000/admin/traffic_violations/vehicle/add/

# generamos token para el user (reemplazar las variables {{}})

```bash
curl --location 'http://localhost:8000/api/token/' \
--header 'Content-Type: application/json' \
--header 'Cookie: csrftoken=rDTeXQiHrqLJEGT1meDujdCXsSlxt4qPPA0q9RRSE78EuuvLb1d3gaCELjuliXHF' \
--data '{
    "username": {{user}},
    "password":{{pass}}
}
'
```
# con la respuesta response {{access}} podremos generar una infraccion (reemplazar las variables {{}})

```bash
curl --location 'http://localhost:8000/cargar_infraccion/' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer {{access}}' \
--header 'Cookie: csrftoken=rDTeXQiHrqLJEGT1meDujdCXsSlxt4qPPA0q9RRSE78EuuvLb1d3gaCELjuliXHF' \
--data '{
    "placa_patente":{{placa_patente}},
    "comentarios": {{comentarios}},
    "timestamp": {{timestamp}}
}'
```

# y ya podremos efectuar la consulta por email
```bash
curl --location 'http://localhost:8000/generar_informe/{{email-person}}' \
--header 'Cookie: csrftoken=rDTeXQiHrqLJEGT1meDujdCXsSlxt4qPPA0q9RRSE78EuuvLb1d3gaCELjuliXHF'
```

## Arquitectura AWS propuesta:

EC2: Para correr los contenedores Docker.
S3: Para almacenamiento de archivos estáticos si es necesario.
IAM: Para gestionar permisos y roles de acceso.
CloudWatch: Para monitoreo y logs.
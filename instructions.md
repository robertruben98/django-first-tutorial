Instrucciones cmd:
- para crear las consultas sql del modelo creado:
    - python manage.py makemigrations
    - python manage.py migrate


Django Rest Framework
    te entrega un marco de trabajo para la creacion de web APIs, ademas de brindarte soporte de autenticacion y
autorizacion. [link](https://www.django-rest-framework.org)
Instalacion: pip install djangorestframework

Http Status Codes en Django
    [Status Code](https://www.django-rest-framework.org/api-guide/status-codes)

Core Arguments y Modelo de Serializacion [link](https://www.django-rest-framework.org/api-guide/fields)

Para visualizer mejor los json [JsonViewer.stack](https://jsonviewer.stack.hu)

El router y el viewset se usan para modelos que no estan compuestos de dos o mas entidades.
Por ejemplo el path de comentario tiene un path complejo

Utilizando postman se pasan las credenciales en Authorization como Basic Auth, y se hace el request

Json Web Token de seguridad tiene:
    header: { 
        tipo token
        algoritmo
    }

    payload: {
        claims: {
            usernamen....
        }
    }

    signature: {
        header, payload, secret-phrase
    }

    token refresh: es valido durante 5 minutos. Es un utilitario para obtener nuevos token de access
    token access: es valido durante 24 horas. Permite consultar la data y hacer las operaciones desde el backend

    [JWT](https://jwt.io) Para ver la informacion de los tokens


Throttling
    Impone restricciones a los request de los usuarios. Puede limitar la cantidad de request por minuto de un usuario


Paginacion con Limit and Offset
    Ejemplo: 100 Records, offset = 60, limit = 5 ----> Records de mi paginacion: desde la posicion 61 hasta 66
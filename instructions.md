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
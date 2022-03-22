

from unicodedata import name
from django.urls import path
from .views import inmueble_list, inmueble_detalle

urlpatterns =[
    path('list/', inmueble_list, name='inmuebles_list'),
    path('<int:pk>', inmueble_detalle, name='inmuebles-detalle'),
]
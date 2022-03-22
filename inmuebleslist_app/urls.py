

from unicodedata import name
from django.urls import path
from .views import inmueble_list

urlpatterns =[
    path('list/', inmueble_list, name='inmuebles_list'),
]
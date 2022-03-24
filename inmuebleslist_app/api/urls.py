from django.urls import path
# from .views import inmueble_list, inmueble_detalle
from .views import InmuebleListAV, InmuebleDetalleAV

urlpatterns =[
    path('list/', InmuebleListAV.as_view(), name='inmuebles_list'),
    path('<int:pk>', InmuebleDetalleAV.as_view(), name='inmuebles-detalle'),
]
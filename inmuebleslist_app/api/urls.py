from django.urls import path
# from .views import inmueble_list, inmueble_detalle
from .views import EdificacionAV, EdificacionDetalleAV, EmpresaAV

urlpatterns =[
    path('list/', EdificacionAV.as_view(), name='edificacion'),
    path('<int:pk>', EdificacionDetalleAV.as_view(), name='edificacion-detalle'),
    path('empresa/', EmpresaAV.as_view(), name='empresa'),
]
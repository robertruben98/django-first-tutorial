from django.urls import path
# from .views import inmueble_list, inmueble_detalle
from .views import EdificacionAV, EdificacionDetalleAV, EmpresaAV, EmpresaDetalleAV, ComentarioList, ComentarioDetail

urlpatterns =[
    path('edificacion/', EdificacionAV.as_view(), name='edificacion'),
    path('edificacion/<int:pk>', EdificacionDetalleAV.as_view(), name='edificacion-detail'),
    
    path('empresa/', EmpresaAV.as_view(), name='empresa'),
    path('empresa/<int:pk>', EmpresaDetalleAV.as_view(), name='empresa-detail'),
    
    path('edificacion/<int:pk>/comentario/', EdificacionDetalleAV.as_view(), name='comentario-list'),
    path('edificacion/comentario/<int:pk>', ComentarioDetail.as_view(), name='comentario-detail'),
]
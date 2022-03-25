from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import (EdificacionAV, EdificacionDetalleAV,
                    ComentarioList, ComentarioDetail, ComentarioCreate, EmpresaVS, UsuarioComentario)

router = DefaultRouter()
router.register('empresa', EmpresaVS, basename='empresa')

urlpatterns = [
    path('edificacion/', EdificacionAV.as_view(), name='edificacion'),
    path('edificacion/<int:pk>', EdificacionDetalleAV.as_view(),
         name='edificacion-detail'),

    path('', include(router.urls)),

    path('edificacion/<int:pk>/comentario-create',
         ComentarioCreate.as_view(), name='comentario-create'),
    path('edificacion/<int:pk>/comentario/',
         ComentarioList.as_view(), name='comentario-list'),
    path('edificacion/comentario/<int:pk>',
         ComentarioDetail.as_view(), name='comentario-detail'),
#     path('edificacion/comentarios/<str:username>/',
#          UsuarioComentario.as_view(), name='usuario-comentario-detail'),
    path('edificacion/comentarios/',
         UsuarioComentario.as_view(), name='usuario-comentario-detail'),
]

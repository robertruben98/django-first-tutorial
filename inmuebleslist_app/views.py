# from django.http import JsonResponse
# from django.shortcuts import render
# from .models import Edificacion

# # Create your views here.
# def inmueble_list(request):
#     inmuebles = Edificacion.objects.all()
#     data = {
#         'inmuebles': list(inmuebles.values()),
#     }
    
#     return JsonResponse(data)

# def inmueble_detalle(request, pk):
#     inmueble = Edificacion.objects.get(pk=pk)
#     data = {
#         'direccion': inmueble.direccion,
#         'pais': inmueble.pais,
#         'imagen': inmueble.imagen,
#         'activo': inmueble.active,
#         'descripcion': inmueble.descripcion
#     }
    
#     return JsonResponse(data)
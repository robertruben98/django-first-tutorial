from ..models import Inmueble
from .serializers import InmuebleSerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view


@api_view()
def inmueble_list(request):
    inmuebles = Inmueble.objects.all()
    serializer = InmuebleSerializer(inmuebles, many=True)
    return Response(serializer.data)


@api_view()
def inmueble_detalle(request, pk):
    inmueble = Inmueble.objects.get(pk=pk)
    serializer = InmuebleSerializer(inmueble)
    return Response(serializer.data)
from ..models import Edificacion, Empresa, Comentario
from .serializers import EdificacionSerializer, EmpresaSerializer, ComentarioSerializer
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from rest_framework import generics, mixins


class ComentarioCreate(generics.CreateAPIView):
    serializer_class = ComentarioSerializer

    def perform_create(self, serializer):
        pk = self.kwargs.get('pk')
        edificacion = Edificacion.objects.get(pk=pk)
        serializer.save(edificacion=edificacion)


class ComentarioList(generics.ListCreateAPIView):
    # queryset = Comentario.objects.all()
    serializer_class = ComentarioSerializer

    def get_queryset(self):
        # kwargs captura todas las propiedades que me manda el cliente
        pk = self.kwargs['pk']
        return Comentario.objects.filter(edificacion=pk)


class ComentarioDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Comentario.objects.all()
    serializer_class = ComentarioSerializer


class EmpresaAV(APIView):
    def get(self, request):
        empresas = Empresa.objects.all()
        serializer = EmpresaSerializer(
            empresas, many=True, context={'request': request})
        return Response(serializer.data)

    def post(self, request):
        serializer = EmpresaSerializer(request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class EmpresaDetalleAV(APIView):
    def get(self, request, pk):
        try:
            empresa = Empresa.objects.get(pk=pk)
        except Empresa.DoesNotExist:
            return Response({'Error': 'Empresa does not exist'}, status=status.HTTP_404_NOT_FOUND)

        serializer = EmpresaSerializer(empresa, context={'request': request})
        return Response(serializer.data)

    def put(self, request, pk):
        try:
            empresa = Empresa.objects.get(pk=pk)
        except Empresa.DoesNotExist:
            return Response({'Error': 'Empresa does not exist'}, status=status.HTTP_404_NOT_FOUND)

        serializer = EmpresaSerializer(
            empresa, data=request.data, context={'request': request})
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        try:
            empresa = Empresa.objects.get(pk=pk)
        except Empresa.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        empresa.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class EdificacionAV(APIView):
    # APIView reconoce que la funcion de nombre get, utiliza el request.method == 'GET'
    def get(self, request):
        inmuebles = Edificacion.objects.all()
        serializer = EdificacionSerializer(inmuebles, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = EdificacionSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class EdificacionDetalleAV(APIView):

    def get(self, request, pk):
        try:
            inmueble = Edificacion.objects.get(pk=pk)
        except Edificacion.DoesNotExist:
            return Response({'Error': 'Edificacion does not exist'}, status=status.HTTP_404_NOT_FOUND)

        serializer = EdificacionSerializer(inmueble)
        return Response(serializer.data)

    def put(self, request, pk):
        try:
            inmueble = Edificacion.objects.get(pk=pk)
        except Edificacion.DoesNotExist:
            return Response({'Error': 'Edificacion does not exist'}, status=status.HTTP_404_NOT_FOUND)

        serializer = EdificacionSerializer(inmueble, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        try:
            inmueble = Edificacion.objects.get(pk=pk)
        except Edificacion.DoesNotExist:
            return Response({'Error': 'Edificacion does not exist'}, status=status.HTTP_404_NOT_FOUND)

        inmueble.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

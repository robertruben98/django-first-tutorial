from ..models import Edificacion, Empresa, Comentario
from .serializers import EdificacionSerializer, EmpresaSerializer, ComentarioSerializer
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from rest_framework import generics, mixins
from rest_framework import viewsets
from django.shortcuts import get_object_or_404
from rest_framework.exceptions import ValidationError
from rest_framework.permissions import IsAuthenticated
from .permissions import IsAdminOrReadOnly, IsComentarioUserOrReadOnly
from rest_framework.throttling import UserRateThrottle, AnonRateThrottle, ScopedRateThrottle
from .throttling import ComentarioCreateThrottle, ComentarioListThrottle


class ComentarioCreate(generics.CreateAPIView):
    serializer_class = ComentarioSerializer
    permission_classes = [IsAuthenticated]
    throttle_classes = [ComentarioCreateThrottle]

    def get_queryset(self):
        return Comentario.objects.all()

    def perform_create(self, serializer):
        pk = self.kwargs.get('pk')
        edificacion = Edificacion.objects.get(pk=pk)

        user = self.request.user
        comentario_queryset = Comentario.objects.filter(
            edificacion=edificacion, comentario_user=user)

        if comentario_queryset.exists():
            raise ValidationError(
                "El usuario ya escribio un comentario para este inmueble")

        if edificacion.number_calificacion == 0:
            edificacion.avg_calificacion = serializer.validated_data['calificacion']
        else:
            edificacion.avg_calificacion = (
                serializer.validated_data['calificacion'] + edificacion.avg_calificacion) / 2

        edificacion.number_calificacion = edificacion.number_calificacion + 1
        edificacion.save()

        serializer.save(edificacion=edificacion, comentario_user=user)


class ComentarioList(generics.ListCreateAPIView):
    # queryset = Comentario.objects.all()
    serializer_class = ComentarioSerializer
    # permission_classes = [IsAuthenticated]
    throttle_classes = [ComentarioListThrottle]

    def get_queryset(self):
        # kwargs captura todas las propiedades que me manda el cliente
        pk = self.kwargs['pk']
        return Comentario.objects.filter(edificacion=pk)


class ComentarioDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Comentario.objects.all()
    serializer_class = ComentarioSerializer
    permission_classes = [IsComentarioUserOrReadOnly]
    throttle_classes = [ScopedRateThrottle]
    throttle_scope = 'comentario-detail'


class EmpresaVS(viewsets.ModelViewSet):
    permission_classes = [IsAdminOrReadOnly]
    queryset = Empresa.objects.all()
    serializer_class = EmpresaSerializer


class EdificacionAV(APIView):
    permission_classes = [IsAdminOrReadOnly]

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
    permission_classes = [IsAdminOrReadOnly]

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

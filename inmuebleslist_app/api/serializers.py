from rest_framework import serializers
from ..models import Edificacion, Empresa, Comentario


class ComentarioSerializer(serializers.ModelSerializer):
    comentario_user = serializers.StringRelatedField(read_only=True)
    class Meta:
        model = Comentario
        exclude = ['edificacion']
        # fields = '__all__'


class EdificacionSerializer(serializers.ModelSerializer):
    comentarios = ComentarioSerializer(many=True, read_only=True)
    empresa_nombre = serializers.CharField(source='empresa.nombre')
    
    class Meta:
        model = Edificacion
        fields = "__all__"


class EmpresaSerializer(serializers.ModelSerializer):
    edificacionlist = EdificacionSerializer(many=True, read_only=True)
    # edificacionlist = serializers.StringRelatedField(many=True, read_only=True) # llama a la funcion __str__ del model
    # edificacionlist = serializers.PrimaryKeyRelatedField(many=True, read_only=True) # para llamar a la pk
    # edificacionlist = serializers.HyperlinkedRelatedField(
    #     many=True, read_only=True, view_name='edificacion-detalle')

    class Meta:
        model = Empresa
        fields = '__all__'

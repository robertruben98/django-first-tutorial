from rest_framework import serializers
from ..models import Edificacion, Empresa


class EdificacionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Edificacion
        fields = "__all__"


class EmpresaSerializer(serializers.HyperlinkedModelSerializer):
    edificacionlist = EdificacionSerializer(many=True, read_only=True)
    # edificacionlist = serializers.StringRelatedField(many=True, read_only=True) # llama a la funcion __str__ del model
    # edificacionlist = serializers.PrimaryKeyRelatedField(many=True, read_only=True) # para llamar a la pk
    # edificacionlist = serializers.HyperlinkedRelatedField(
    #     many=True, read_only=True, view_name='edificacion-detalle')

    class Meta:
        model = Empresa
        fields = '__all__'

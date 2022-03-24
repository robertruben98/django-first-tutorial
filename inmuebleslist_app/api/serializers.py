from rest_framework import serializers
from ..models import Edificacion, Empresa


class EmpresaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Empresa
        fields = '__all__'



class EdificacionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Edificacion
        fields = "__all__"
        
        
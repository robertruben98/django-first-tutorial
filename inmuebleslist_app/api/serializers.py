from rest_framework import serializers
from ..models import Inmueble


# ModelSerializer hace un mapeo automatico de los campos de la entidad Inmueble
class InmuebleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Inmueble
        fields = "__all__"
        # fields = ['id', 'pais', 'imagen', 'active']
        # exclude = ['id']
        
    def validate(self, data):
        if data['direccion'] == data['pais']:
            raise serializers.ValidationError('La direccion y el pais deben ser diferentes')
        else:
            return data
        
    def validate_imagen(self, data):
        if len(data) < 2:
            raise serializers.ValidationError('La url de la imagen es muy corta')
        else:
            return data
    


# def column_longitud(value):
#     if len(value) < 2:
#         raise serializers.ValidationError('El valor es demasiado corto')


# class InmuebleSerializer(serializers.Serializer):
#     id = serializers.IntegerField(read_only=True)
#     direccion = serializers.CharField(validators=[column_longitud])
#     pais = serializers.CharField(validators=[column_longitud])
#     descripcion = serializers.CharField()
#     imagen = serializers.CharField()
#     active = serializers.BooleanField()
    
#     def create(self, validated_data):
#         return Inmueble.objects.create(**validated_data) # retornar todos los argumentos que corresponden al validated data
    
#     def update(self, instance, validated_data):
#         instance.direccion = validated_data.get('direccion', instance.direccion)
#         instance.pais = validated_data.get('pais', instance.pais)
#         instance.descripcion = validated_data.get('descripcion', instance.descripcion)
#         instance.imagen = validated_data.get('imagen', instance.imagen)
#         instance.active = validated_data.get('active', instance.active)
#         instance.save()
#         return instance
    
#     def validate(self, data):
#         if data['direccion'] == data['pais']:
#             raise serializers.ValidationError('La direccion y el pais deben ser diferentes')
#         else:
#             return data
        
#     # validate es el patron, _imagen es el nombre de la propiedad que quieres validar
#     def validate_imagen(self, data):
#         if len(data) < 2:
#             raise serializers.ValidationError('La url de la imagen es muy corta')
#         else:
#             return data
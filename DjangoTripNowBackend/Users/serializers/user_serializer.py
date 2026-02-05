
from rest_framework import serializers

from Users.models import CustomUser


class UserSerializer(serializers.ModelSerializer):
    nombre = serializers.CharField(max_length=100, required=True)


    def validate(self, data):            #para validar los datos
        nombre = data.get('nombre')

        if not nombre:
            raise serializers.ValidationError("El nombre es obligatorio")

        return data


    def post(self, request):
        pass
    


    class Meta:
        model = CustomUser
        fields = ('nombre',) #la coma es para la tupla


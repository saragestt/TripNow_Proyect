

from rest_framework import serializers
import re

from rest_framework_simplejwt.tokens import RefreshToken

from Users.models import CustomUser, InfoModel


class registerSerializer(serializers.Serializer):
    nombre = serializers.CharField(max_length=50, null=False, blank=False)
    apellidos = serializers.CharField(max_length=50, required=False, blank=False)
    email = serializers.EmailField(min_length=5, unique=True, blank=False, null=False)
    direccion = serializers.CharField(max_length=100, blank=False, null=False)
    telefono = serializers.CharField(max_length=10, blank=False, null=False)
    fecha_nacimiento = serializers.DateField(max_length=10, blank=False, null=False)
    nacionalidad = serializers.CharField(max_length=30, blank=False, null=False)
    pasaporte = serializers.CharField(max_length=30, blank=True, null=True)
    codigo_postal = serializers.CharField(max_length=10, blank=True, null=True)
    password = serializers.CharField(min_length=6, max_length=100, required=True)
    password1 = serializers.CharField(min_length=6, max_length=100, required=True)

    class Meta:
        model = CustomUser, InfoModel
        fields = ('nombre', 'apellidos','email', 'direccion', 'telefono', 'fecha_nacimiento', 'nacionalidad', 'pasaporte', 'codigo_postal')


    def validate_email(self, email):
        if CustomUser.objects.filter(email=email).exists():
            raise serializers.ValidationError("Ya existe un usuario con este email")
        return email

    def validate_password(self, password):
        if password == "":
            raise serializers.ValidationError("La contraseña es obligatoria")

        if len(password) < 6:
            raise serializers.ValidationError("La contraseña debe contener al menos 6 caracteres")

        patron = r"^(?=.*[A-Za-z])(?=.*\d)(?=.*[@$!%*?&])[A-Za-z\d@$!%*?&]{6,}$"

        if re.match(patron, password):
            raise serializers.ValidationError('Contraseña no valida')

        return password

    def validate_telefono(self, telefono):
        if InfoModel.objects.filter(telefono=telefono).exists():
            raise serializers.ValidationError("Ya existe un usuario con este telefono")
        return telefono

    def validate_pasaporte(self, pasaporte):
        if InfoModel.objects.filter(pasaporte=pasaporte).exists():
            raise serializers.ValidationError("Ya existe un usuario con este pasaporte")


    def validate(self, data):

        if data['password'] != data['password1']:
            raise serializers.ValidationError("Las contraseñas no coinciden")

        return {
            'sucess': True,
            'message': 'Usuario registrado con exito',
        }

    def save(self, validate_data):
        info_personal = InfoModel.objects.create(direccion=validate_data['direccion'],
                                         telefono=validate_data['telefono'],
                                         fecha_nacimiento=validate_data['fecha_nacimiento'],
                                         nacionalidad=validate_data['nacionalidad'],
                                         pasaporte=validate_data['pasaporte'],
                                         codigo_postal=validate_data['codigo_postal'])

        user = CustomUser.objects.create(nombre=validate_data['nombre'],
                                         apellidos=validate_data['apellidos'],
                                         email=validate_data['email'],
                                         info_personal=info_personal)

        user.set_password(validate_data['password']) #set password para encriptar
        info_personal.save()
        user.save()

        return user



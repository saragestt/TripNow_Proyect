from os import access

from rest_framework import serializers
import re

from rest_framework_simplejwt.tokens import RefreshToken

from Users.models import CustomUser


class LoginSerializer(serializers.Serializer):
    email = serializers.EmailField(max_length=100, required=True)
    password = serializers.CharField(min_length=5, max_length=100, required=True)

    class Meta:
        model = CustomUser
        fields = ('email', 'password')


    def validate_email(self, email):
        if email == "":
            raise serializers.ValidationError("Email obligatorio")

        if "@" not in email:
            raise serializers.ValidationError("@ is required")

        return email



    def validate_password(self, password):
        if password == "":
            raise serializers.ValidationError("Password required")

        if len(password) < 4:
            raise serializers.ValidationError("Password must be at least 5 characters long")

        patron = r"^(?=.*[A-Za-z])(?=.*\d)(?=.*[@$!%*?&])[A-Za-z\d@$!%*?&]{4,}$"

        if re.match(patron, password):
            raise serializers.ValidationError('Contraseña no valida')

        return password



    def validate(self, data): #data es lo que viene del front
        email = data.get("email",'')
        password = data.get("password",'')

        user = CustomUser.objects.filter(email=email).first() #si email(rojo) es gual al user lle da el primero

        if not user:
            raise serializers.ValidationError("No existe el usuario")

        if not user.check_password(password): #el check_password veirifca si coincide con la  contraseña encriptada
            raise serializers.ValidationError("Contraseña incorrecta")

        refresh_token = RefreshToken.for_user(user) #solo es para login
        access_token =  refresh_token.access_token

        return {
            'sucess': True,
            'message': f"Bienvenido {user.nombre}",
            'data': {
                'nombre': user.nombre,
            },
                'access_token': str(access_token),
                'refresh_token': str(refresh_token),

            }



    #aqui no ponemos save porque no vamos a guardarlo, en register sip
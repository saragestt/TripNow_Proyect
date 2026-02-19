from rest_framework import serializers


from Viajes.models import ImagenReseñas, ReseñasModel, AlojamientoModel

class AddReseñaSerializer(serializers.ModelSerializer):
    identificador = serializers.CharField(required=True)
    usuario = serializers.CharField(required=True)
    alojamiento = serializers.CharField(required=True)
    descripcion = serializers.CharField(required=True)
    puntuacion = serializers.IntegerField(required=True)
    imagen = serializers.ImageField(write_only=True)


    class Meta:
        model = ReseñasModel
        fields = ('identificador', 'usuario', 'alojamiento', 'descripcion', 'puntuacion', 'imagen')


    def validate(self, attrs):
        return attrs

    def create(self, validated_data):
        reseñas_obj = ReseñasModel.objects.filter(slug=validated_data['identificador']).first()
        if not reseñas_obj:
            raise serializers.ValidationError("El identificador no existe")


        reseña = ReseñasModel.objects.create(
            identificador=validated_data['identificador'],
            usuario=validated_data['usuario'],
            alojamiento=validated_data['alojamiento'],
            descripcion=validated_data['descripcion'],
            puntuacion=validated_data['puntuacion'],

        )

        imagen = ImagenReseñas.objects.create(
            imagen=validated_data['imagen'],
        )

        imagen.save()
        return reseña
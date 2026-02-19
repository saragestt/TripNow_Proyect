from rest_framework import serializers

from Viajes.models import ImagenAlojamiento,CategoriaAlojamiento,AlojamientoModel

class AddAlojamientoSerializer(serializers.ModelSerializer):
    identificador = serializers.CharField(required=True)
    nombre_alojamiento = serializers.CharField(required=True)
    fecha_llegada = serializers.DateField(required=True)
    fecha_salida = serializers.DateField(required=True)
    ciudad = serializers.CharField(required=True)
    precio = serializers.DecimalField(required=True, max_digits=10, decimal_places=2)
    categoria_alojamiento = serializers.CharField(required=True)

    class Meta:
        model = AlojamientoModel
        fields = ('identificador', 'nombre_alojamiento', 'fecha_llegada', 'fecha_salida', 'precio', 'categoria_alojamiento', 'ciudad', 'precio', 'categoria_alojamiento')

    def validate(self, attrs):
        return attrs

    def create(self, validated_data):
        categoria_alojamiento_obj = CategoriaAlojamiento.objects.filter(slug=validated_data['categoria_alojamiento']).first()

        if not categoria_alojamiento_obj:
            raise serializers.ValidationError('La categoria alojamiento no existe')

        alojamiento = AlojamientoModel.objects.create(
            identificador=validated_data['identificador'],
            nombre_alojamiento=validated_data['nombre_alojamiento'],
            fecha_llegada=validated_data['fecha_llegada'],
            fecha_salida=validated_data['fecha_salida'],
            precio=validated_data['precio'],
            ciudad=validated_data['ciudad'],
            categoria_alojamiento=validated_data['categoria_alojamiento'],

        )
        imagen_alojamiento = ImagenAlojamiento.objects.create(
            alojamiento=alojamiento,
            imagen_alojamiento=validated_data['imagen alojamiento'],
        )

        imagen_alojamiento.save()
        return alojamiento

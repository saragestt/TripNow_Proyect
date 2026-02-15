from rest_framework import serializers

from Viajes.models import ImagenViaje, Viaje, Categoria

class AddViajeSerializer(serializers.ModelSerializer):
    identificador = serializers.CharField(required=True)
    ciudad_salida = serializers.CharField(required=True, max_length=100)
    ciudad_llegada = serializers.CharField(required=True, max_length=100)

    terminal_salida = serializers.CharField(required=True, max_length=100)
    terminal_llegada = serializers.CharField(required=True, max_length=100)

    lugar_salida = serializers.CharField(required=True, max_length=100)
    lugar_llegada = serializers.CharField(required=True, max_length=100)

    fecha_salida = serializers.DateField(required=True)
    fecha_llegada = serializers.DateField(required=True)

    precio = serializers.DecimalField(max_digits=10, decimal_places=2, required=True)
    categoria = serializers.CharField(required=True)
    imagen = serializers.ImageField(write_only=True)

    class Meta:
        model = Viaje
        fields = ('identificador', 'ciudad_salida', 'ciudad_llegada', 'terminal_salida', 'terminal_llegada', 'lugar_salida', 'lugar_llegada', 'fecha_salida','fecha_llegada', 'precio', 'categoria', 'imagen')

    def validate(self, attrs):
        return attrs

    def create(self, validated_data):
        categoria_obj = Categoria.objects.filter(slug=validated_data["categoria"]).first()
        if not categoria_obj:
            raise serializers.ValidationError("La categoria no existe.")

        viaje = Viaje.objects.create(
            identificador=validated_data["identificador"],
            ciudad_salida=validated_data["ciudad_salida"],
            ciudad_llegada=validated_data["ciudad_llegada"],
            terminal_salida=validated_data["terminal_salida"],
            terminal_llegada=validated_data["terminal_llegada"],
            lugar_salida=validated_data["lugar_salida"],
            lugar_llegada=validated_data["lugar_llegada"],
            fecha_salida=validated_data["fecha_salida"],
            fecha_llegada=validated_data["fecha_llegada"],
            precio=validated_data["precio"],
            categoria=validated_data["categoria"],
        )
        imagen = ImagenViaje.objects.create(
            viaje=viaje,
            imagen=validated_data["imagen"],

        )

        imagen.save()
        return viaje

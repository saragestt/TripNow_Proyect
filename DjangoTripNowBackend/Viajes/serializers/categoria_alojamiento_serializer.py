from rest_framework import serializers

from Viajes.models import CategoriaAlojamiento

class CategoriaAlojamientoSerializer(serializers.ModelSerializer):
    class Meta:
        model = CategoriaAlojamiento
        fields = ('nombre','slug')
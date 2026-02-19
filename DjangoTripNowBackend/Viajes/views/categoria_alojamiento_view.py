from rest_framework import status
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView
from Viajes.models import CategoriaAlojamiento
from Viajes.serializers import CategoriaAlojamientoSerializer




class CategoriaAlojamientoView(APIView):
    permission_classes = [AllowAny]

    def get(self,request):
        categorias_alojamiento = CategoriaAlojamiento.objects.all().order_by('nombre')
        data1 = CategoriaAlojamientoSerializer(categorias_alojamiento,many=True).data

        data = [{"nombre": categoria_a.nombre,
                 "slug": categoria_a.slug,
                 }
                for categoria_a in categorias_alojamiento
                ]

        return Response({"data": data1}, status=status.HTTP_200_OK)
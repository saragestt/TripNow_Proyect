from rest_framework import status
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView


from Viajes.models import Categoria
from Viajes.serializers import CategoriaSerializer


class CategoriaView(APIView):
    permission_classes = [AllowAny]

    def get(self,request):
        categorias = Categoria.objects.all().order_by('nombre')
        data1 = CategoriaSerializer(categorias,many=True).data

        data = [{"nombre": categoria.nombre,
                 "slug": categoria.slug,
                 }
                for categoria in categorias
                ]

        return Response({"data": data1}, status=status.HTTP_200_OK)
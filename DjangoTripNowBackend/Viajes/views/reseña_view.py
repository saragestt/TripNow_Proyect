from rest_framework import status
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView

from Viajes.models import ReseñasModel
from Viajes.serializers import AddReseñaSerializer


class ReseñaView(APIView):
    permission_classes = (AllowAny,)
    parser_classes = (MultiPartParser, FormParser)


    def get(self, request):
        reseñas = ReseñasModel.objects.select_related("Imagen_reseña").order_by('identificador')

        data = [
            {
                "identificador": reseña.identificador,
                "usuario": reseña.usuario.nombre,
                "alojamiento": reseña.alojamiento.nombre_alojamiento,
                "slug_resenia": reseña.slug,
                "descripcion": reseña.descripcion,
                "puntuacion": reseña.puntuacion,
                "imagen": "" if not reseña.Imagen_reseña.imagen.url else request.build_absolute_uri(reseña.Imagen_reseña.imagen.url)
            }
            for reseña in reseñas
        ]
        print(data)
        return Response({"data": data, "success": True}, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = AddReseñaSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

from rest_framework import status
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from Viajes.models import Viaje

class ViajeView(APIView):
    permission_classes = [AllowAny]

    def get(self,request):
        viajes = Viaje.objects.filter(is_active=True).order_by('-categoria', 'identificador')

        data = [
            {
                "identificador": viaje.identificador,
                "ciudad_salida": viaje.ciudad_salida,
                "ciudad_llegada": viaje.ciudad_llegada,
                "terminal_salida": viaje.terminal_salida,
                "terminal_llegada": viaje.terminal_llegada,
                "lugar_salida": viaje.lugar_salida,
                "lugar_llegada": viaje.lugar_llegada,
                "fecha_salida": viaje.fecha_salida,
                "fecha_llegada": viaje.fecha_llegada,
                "precio": viaje.precio,
                "nombre_categoria": viaje.categoria.nombre,
                "slug_categoria": viaje.categoria.slug,
                "slug_viaje": viaje.slug,
                "imagen": "" if not viaje.imagen.imagen.url else request.build_absolute_uri(viaje.imagen.imagen.url)

            }
            for viaje in viajes
        ]

        return Response({"data": data, "success": True}, status=status.HTTP_200_OK)
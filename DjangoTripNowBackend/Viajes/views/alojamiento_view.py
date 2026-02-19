from rest_framework import status
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView

from Viajes.models import AlojamientoModel

class AlojamientoView(APIView):
    permission_classes = [AllowAny]

    def get(self,request):
        alojamientos = AlojamientoModel.objects.filter(is_active=True).order_by('-categoria_alojamiento__nombre', 'identificador')

        data = [
            {
                "identificador": alojamiento.identificador,
                "nombre_alojamiento": alojamiento.nombre_alojamiento,
                "fecha_llegada": alojamiento.fecha_llegada,
                "fecha_salida": alojamiento.fecha_salida,
                "ciudad": alojamiento.ciudad,
                "precio": alojamiento.precio,
                "nombre_categoria_alojamiento":alojamiento.categoria_alojamiento.nombre,
                "slug_categoria_alojamiento":alojamiento.categoria_alojamiento.slug,
                "slug_alojamiento": alojamiento.slug,
                "imagen": "" if not alojamiento.imagen.imagen.url else request.build_absolute_uri(alojamiento.imagen.imagen.url)

            }
            for alojamiento in alojamientos
        ]


        return Response({"data": data, "success": True}, status=status.HTTP_200_OK)
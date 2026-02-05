from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from Users.models import CustomUser
from Users.serializers.user_serializer import UserSerializer


class UserView(APIView):


    def get(self, request):
        user = CustomUser.objects.all()
        user_serializer = UserSerializer(user, many=True) #many es para decirle si son muchos
        return Response(user_serializer.data, status=status.HTTP_200_OK ) #.data es donde estan los datos



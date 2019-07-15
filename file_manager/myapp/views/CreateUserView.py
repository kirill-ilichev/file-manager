from django.conf import settings
from myapp.serializers import UserSerializer
from rest_framework import status
from myapp.models import User
import jwt
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from rest_framework_jwt.utils import jwt_payload_handler


class CreateUserView(APIView):
    permission_classes = (AllowAny, )

    def post(self, request):
        user = request.data
        serializer = UserSerializer(data=user)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        email = request.data['email']
        password = request.data['password']
        user = User.objects.get(email=email, password=password)

        token = jwt.encode(jwt_payload_handler(user), settings.SECRET_KEY)
        user_details = {'token': token}

        return Response(user_details, status=status.HTTP_201_CREATED)

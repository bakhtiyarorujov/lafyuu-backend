from django.shortcuts import render
from .serializers import UserRegisterSerializer
from rest_framework import generics, permissions, status
from django.contrib.auth import get_user_model
from rest_framework.views import APIView
from django.contrib.auth import authenticate, login
from rest_framework.response import Response
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi


User = get_user_model()

# Create your views here.

class UserRegisterAPI(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserRegisterSerializer
    permission_classes = [permissions.AllowAny]


class UserLoginAPI(APIView):
    permission_classes = [permissions.AllowAny]

    @swagger_auto_schema(
        request_body=openapi.Schema(
            type=openapi.TYPE_OBJECT,
            properties={
                'email': openapi.Schema(type=openapi.TYPE_STRING),
                'password': openapi.Schema(type=openapi.TYPE_STRING, format='password'),
            },
            required=['email', 'password'],
        ),
        responses={
            200: openapi.Response('Successful login', UserRegisterSerializer),
            400: 'Invalid credentials',
        },
    )

    def post(self, request):
        email = request.data.get('email')
        password = request.data.get('password')
        user = authenticate(request, email=email, password=password)

        if user:
            login(request, user)
            serializer = UserRegisterSerializer(instance=user)
            return Response(serializer.data)
        return Response({'detail': 'Username or Password is wrong!'}, status=status.HTTP_400_BAD_REQUEST)
    
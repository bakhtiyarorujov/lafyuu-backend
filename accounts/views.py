from .serializers import (
    UserRegisterSerializer,
    UserLoginSerializer)
from rest_framework import generics, permissions, status
from django.contrib.auth import get_user_model
from rest_framework.views import APIView
from django.contrib.auth import authenticate, login
from rest_framework.response import Response
from drf_spectacular.utils import extend_schema


User = get_user_model()

# Create your views here.

class UserRegisterAPI(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserRegisterSerializer
    permission_classes = [permissions.AllowAny]


@extend_schema(
    request=UserLoginSerializer,
    methods=['POST'],
)
class UserLoginAPI(APIView):
    permission_classes = [permissions.AllowAny]

    def post(self, request):
        email = request.data.get('email')
        password = request.data.get('password')
        user = authenticate(request, email=email, password=password)

        if user:
            login(request, user)
            serializer = UserRegisterSerializer(instance=user)
            return Response(serializer.data)
        return Response({'detail': 'Username or Password is wrong!'}, status=status.HTTP_400_BAD_REQUEST)
    
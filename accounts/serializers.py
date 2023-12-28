from rest_framework import serializers
from django.contrib.auth import get_user_model
from rest_framework.authtoken.models import Token

User = get_user_model()

class UserRegisterSerializer(serializers.ModelSerializer):
    token = serializers.SerializerMethodField()
    class Meta:
        model = User
        fields = (
            'token',
            'id',
            'full_name',
            'email',
            'password'
        )
        extra_kwargs = {
            'password': {'write_only': True}
        }

    def get_token(self, instance):
        return Token.objects.get_or_create(user=instance)[0].key


    def create(self, validated_data):
        user = User.objects.create_user(
            username=validated_data['email'],  # Use email or another field as the username
            email=validated_data['email'],
            full_name=validated_data['full_name'],
            password=validated_data['password']
        )
        return user
    

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = (
            'id',
            'email',
            'fullname'
        )

class UserLoginSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = (
            'email',
            'password'
        )
        extra_kwargs = {
            'password': {'write_only': True}
        }
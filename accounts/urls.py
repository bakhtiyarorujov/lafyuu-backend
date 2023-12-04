from django.urls import path
from .views import (
    UserRegisterAPI,
    UserLoginAPI)

urlpatterns = [
    path('register', UserRegisterAPI.as_view(), name='user_register'),
    path('login', UserLoginAPI.as_view(), name='user_login'),
]
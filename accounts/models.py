from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
GENDER_CHOICES = (
    ('ML', 'Male'),
    ('FM', 'Female')
)

class User(AbstractUser):
    image = models.ImageField(upload_to='media/users', null=True, blank=True)
    birthday = models.DateField(null=True, blank=True)
    gender = models.CharField(max_length=2, choices=GENDER_CHOICES, null=True, blank=True)
    email = models.EmailField(unique=True)
    full_name = models.CharField(max_length=50)
    username = models.CharField(max_length=50, null=True, blank=True)
    first_name = None
    last_name = None

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['full_name', 'username']
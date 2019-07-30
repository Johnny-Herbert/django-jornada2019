from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.

class User(AbstractUser):
    email = models.EmailField(unique=True)
    picture = models.ImageField('Imagem de perfil', default='/img/userpicture.png')
    create_at = models.DateTimeField(auto_now_add=True)
from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.

class User(AbstractUser):
    email = models.EmailField(unique=True)
    picture = models.ImageField('Imagem de perfil', default='/img/userpicture.png')
    following = models.ManyToManyField('self', verbose_name='Seguindo', related_name='following_users', blank=True, symmetrical=False)
    followers = models.ManyToManyField('self', verbose_name='Seguidores', related_name='followers_users', blank=True, symmetrical=False)
    create_at = models.DateTimeField(auto_now_add=True)
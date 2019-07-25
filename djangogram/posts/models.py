from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Post(models.Model):
    auth = models.ForeignKey('users.User', on_delete=models.CASCADE, verbose_name='Autor')
    image = models.ImageField(verbose_name='Imagem', upload_to='posts/')
    description = models.CharField(max_length=256, verbose_name='Descrição')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Criado em')
    modified_at = models.DateTimeField(auto_now=True, verbose_name='Modificado em')

    def __str__(self):
        return f'Post {self.pk} | Author {self.auth} | Created at {self.created_at}'
    
    class Meta:
        verbose_name = 'Postagem'
        verbose_name_plural = 'Postagens'
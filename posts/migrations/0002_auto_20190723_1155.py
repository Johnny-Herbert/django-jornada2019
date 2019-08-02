# Generated by Django 2.2.3 on 2019-07-23 14:55

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='post',
            options={'verbose_name': 'Postagem', 'verbose_name_plural': 'Postagens'},
        ),
        migrations.AlterField(
            model_name='post',
            name='auth',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Autor'),
        ),
        migrations.AlterField(
            model_name='post',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, verbose_name='Criado em'),
        ),
        migrations.AlterField(
            model_name='post',
            name='description',
            field=models.CharField(max_length=256, verbose_name='Descrição'),
        ),
        migrations.AlterField(
            model_name='post',
            name='image',
            field=models.ImageField(upload_to='', verbose_name='Imagem'),
        ),
        migrations.AlterField(
            model_name='post',
            name='modified_at',
            field=models.DateTimeField(auto_now=True, verbose_name='Modificado em'),
        ),
    ]
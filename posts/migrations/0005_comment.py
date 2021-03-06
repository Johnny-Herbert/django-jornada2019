# Generated by Django 2.2.3 on 2019-07-29 12:33

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('posts', '0004_auto_20190726_0957'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField(verbose_name='Texto')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Criado em')),
                ('auth', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='commentsFromUser', to=settings.AUTH_USER_MODEL, verbose_name='Autor')),
                ('post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='commentsFromPost', to='posts.Post', verbose_name='Post')),
            ],
            options={
                'verbose_name': 'Comentário',
                'verbose_name_plural': 'Comentarios',
            },
        ),
    ]

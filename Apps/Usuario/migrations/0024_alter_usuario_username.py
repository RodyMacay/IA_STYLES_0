# Generated by Django 4.2.7 on 2023-11-16 00:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Usuario', '0023_perfil_imagen_usuario_alter_perfil_usuario_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usuario',
            name='username',
            field=models.CharField(max_length=150, unique=True),
        ),
    ]

# Generated by Django 4.2.7 on 2023-11-16 21:25

import Apps.Usuario.utils
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Usuario', '0024_alter_usuario_username'),
    ]

    operations = [
        migrations.AlterField(
            model_name='perfil',
            name='imagen',
            field=models.ImageField(blank=True, null=True, upload_to=Apps.Usuario.utils.user_media_path),
        ),
    ]

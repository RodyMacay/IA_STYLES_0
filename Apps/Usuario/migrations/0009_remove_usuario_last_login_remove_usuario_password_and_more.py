# Generated by Django 4.2.7 on 2023-11-04 03:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Usuario', '0008_remove_usuario_contra_usuario_last_login_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='usuario',
            name='last_login',
        ),
        migrations.RemoveField(
            model_name='usuario',
            name='password',
        ),
        migrations.AddField(
            model_name='usuario',
            name='contra',
            field=models.CharField(default='001', max_length=200),
        ),
    ]

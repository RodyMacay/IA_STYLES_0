# Generated by Django 4.2.7 on 2023-11-08 22:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Usuario', '0014_remove_usuarios_groups_remove_usuarios_is_active_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='usuarios',
            name='last_login',
        ),
        migrations.RemoveField(
            model_name='usuarios',
            name='password',
        ),
        migrations.AddField(
            model_name='usuarios',
            name='contra',
            field=models.CharField(default=1, max_length=200),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='usuarios',
            name='nomusuario',
            field=models.CharField(max_length=50),
        ),
    ]

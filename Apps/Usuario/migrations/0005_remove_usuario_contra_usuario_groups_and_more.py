# Generated by Django 4.2.7 on 2023-11-04 03:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
        ('Usuario', '0004_remove_usuario_loginid'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='usuario',
            name='contra',
        ),
        migrations.AddField(
            model_name='usuario',
            name='groups',
            field=models.ManyToManyField(blank=True, related_name='custom_user_set', to='auth.group'),
        ),
        migrations.AddField(
            model_name='usuario',
            name='is_active',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='usuario',
            name='is_staff',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='usuario',
            name='is_superuser',
            field=models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status'),
        ),
        migrations.AddField(
            model_name='usuario',
            name='last_login',
            field=models.DateTimeField(blank=True, null=True, verbose_name='last login'),
        ),
        migrations.AddField(
            model_name='usuario',
            name='password',
            field=models.CharField(default='pbkdf2_sha256$600000$6hKgVTEAotkzuqPnQT2mjg$w5c25Z185zzEHIm4dF5wpUfs3+8P8YkhHo3CQwrwpY8=', max_length=128),
        ),
        migrations.AddField(
            model_name='usuario',
            name='user_permissions',
            field=models.ManyToManyField(blank=True, related_name='custom_user_set', to='auth.permission'),
        ),
        migrations.AlterField(
            model_name='usuario',
            name='correo',
            field=models.EmailField(max_length=50, unique=True),
        ),
        migrations.AlterField(
            model_name='usuario',
            name='nomusuario',
            field=models.CharField(max_length=50, unique=True),
        ),
    ]

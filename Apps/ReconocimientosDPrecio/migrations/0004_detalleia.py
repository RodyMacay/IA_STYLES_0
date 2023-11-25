# Generated by Django 4.2.7 on 2023-11-16 23:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ReconocimientosDPrecio', '0003_alter_imagenes_usuario'),
    ]

    operations = [
        migrations.CreateModel(
            name='DetalleIA',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('marca', models.CharField(max_length=50)),
                ('talla', models.IntegerField(default=None, null=True)),
                ('precio', models.IntegerField()),
                ('descripcion', models.CharField(max_length=150)),
                ('condicion', models.CharField(max_length=50)),
                ('tipo', models.CharField(max_length=50)),
                ('imagen', models.OneToOneField(null=True, on_delete=django.db.models.deletion.SET_NULL, to='ReconocimientosDPrecio.imagenes')),
            ],
        ),
    ]
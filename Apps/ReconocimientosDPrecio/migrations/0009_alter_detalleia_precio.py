# Generated by Django 4.2.7 on 2023-12-06 23:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ReconocimientosDPrecio', '0008_alter_detalleia_precio'),
    ]

    operations = [
        migrations.AlterField(
            model_name='detalleia',
            name='precio',
            field=models.IntegerField(),
        ),
    ]

# Generated by Django 4.2.7 on 2023-12-08 23:04

from django.db import migrations
import djmoney.models.fields


class Migration(migrations.Migration):

    dependencies = [
        ('ReconocimientosDPrecio', '0012_alter_detalleia_precio_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='detalleia',
            name='precio',
            field=djmoney.models.fields.MoneyField(blank=True, decimal_places=2, max_digits=10, null=True),
        ),
    ]

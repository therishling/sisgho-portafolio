# Generated by Django 3.0.6 on 2020-06-22 03:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0011_factura_empleado'),
    ]

    operations = [
        migrations.AddField(
            model_name='pedido',
            name='iva',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='pedido',
            name='subtotal',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='pedido',
            name='total',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
    ]

# Generated by Django 3.0.6 on 2020-06-19 05:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0007_auto_20200611_1243'),
    ]

    operations = [
        migrations.AddField(
            model_name='factura',
            name='iva',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='factura',
            name='subtotal',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='factura',
            name='total',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
    ]
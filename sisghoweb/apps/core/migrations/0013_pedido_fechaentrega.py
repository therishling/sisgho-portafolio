# Generated by Django 3.0.6 on 2020-06-22 03:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0012_auto_20200621_2315'),
    ]

    operations = [
        migrations.AddField(
            model_name='pedido',
            name='fechaentrega',
            field=models.DateField(blank=True, null=True),
        ),
    ]

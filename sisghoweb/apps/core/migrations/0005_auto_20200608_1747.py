# Generated by Django 3.0.6 on 2020-06-08 21:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_auto_20200608_1318'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='detallefactura',
            name='serviciocomedor',
        ),
        migrations.AddField(
            model_name='detallefactura',
            name='detallereserva',
            field=models.ForeignKey(blank=True, db_column='detallereserva', null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='core.DetalleReserva'),
        ),
        migrations.AddField(
            model_name='detallefactura',
            name='solicitudcompra',
            field=models.ForeignKey(blank=True, db_column='solicitudcompra', null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='core.SolicitudCompra'),
        ),
    ]

# Generated by Django 3.0.6 on 2020-06-20 02:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0008_auto_20200619_0102'),
    ]

    operations = [
        migrations.AddField(
            model_name='huesped',
            name='empleado',
            field=models.ForeignKey(blank=True, db_column='empleado', null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='core.Empleado'),
        ),
    ]
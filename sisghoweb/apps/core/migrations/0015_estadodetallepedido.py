# Generated by Django 3.0.6 on 2020-06-29 06:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0014_usuario_is_active'),
    ]

    operations = [
        migrations.CreateModel(
            name='EstadoDetallePedido',
            fields=[
                ('idestado', models.AutoField(primary_key=True, serialize=False)),
                ('descripcion', models.CharField(max_length=100)),
            ],
            options={
                'db_table': 'estadodetallepedido',
            },
        ),
    ]

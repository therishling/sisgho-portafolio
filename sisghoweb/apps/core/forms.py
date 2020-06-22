from django import forms
from django.contrib.auth.forms import ReadOnlyPasswordHashField, UserChangeForm
from apps.core import models as modelo
from datetime import date


class HuespedForm(forms.ModelForm):
    class Meta:
        model = modelo.Huesped
        fields = ('nombre', 'apellidopaterno', 'apellidomaterno',
                  'rut', 'fechadesde', 'fechahasta', 'cliente')


class AsHabitacionForm(forms.ModelForm):
    class Meta:
        model = modelo.Huesped
        fields = ('habitacion',)


class DetalleReservaForm(forms.ModelForm):
    class Meta:
        model = modelo.DetalleReserva
        fields = ('habitacion',)


class SolicitudCompraForm(forms.ModelForm):
    class Meta:
        model = modelo.SolicitudCompra
        fields = ('cantidad',)


class FacturaForm(forms.ModelForm):
    class Meta:
        model = modelo.Factura
        fields = ('fechapago',)


class PedidoForm(forms.ModelForm):
    class Meta:
        model = modelo.Pedido
        fields = ('observaciones',)


class HabitacionForm(forms.Form):

    def actualizar_estado(self):
        huespedes = modelo.Huesped.objects.all().filter(habitacion__isnull=False).order_by('idhuesped')
        for huesped in huespedes:
            if huesped.fechahasta < date.today():
                habitacion = modelo.Habitacion.objects.get(
                    idhabitacion=huesped.habitacion.idhabitacion)
                habitacion.estadohabitacion = modelo.Estadohabitacion.objects.get(
                    idestado=1)
                habitacion.save()
            if huesped.fechahasta > date.today():
                habitacion = modelo.Habitacion.objects.get(
                    idhabitacion=huesped.habitacion.idhabitacion)
                habitacion.estadohabitacion = modelo.Estadohabitacion.objects.get(
                    idestado=2)
                habitacion.save()

from django import forms
from django.contrib.auth.forms import ReadOnlyPasswordHashField, UserChangeForm
from apps.core import models as modelo
from datetime import date
from django.contrib.auth.forms import AuthenticationForm, PasswordResetForm

class HuespedForm(forms.ModelForm):
    class Meta:
        model = modelo.Huesped
        fields = ('nombre', 'apellidopaterno', 'apellidomaterno',
                  'rut', 'fechadesde', 'fechahasta', 'cliente')
    
   

    def __init__(self, *args, **kwargs):
        super(HuespedForm, self).__init__(*args, **kwargs)
        if self.data:
            # make the QueryDict mutable
            self.data = self.data.copy()
            # remove dots from data["cpf"]
            if "rut" in self.data:
                self.data["rut"] = self.data["rut"].replace(".", "")
        # ...


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

class FormLogin(AuthenticationForm):
    error_messages = {
        'invalid_login': (
            "Porfavor ingrese un nombre de usuario o contraseña correcto. "
        ),
        'inactive': ("This account is inactive."),
    }

class PerfilForm(forms.ModelForm):
    class Meta:
        model = modelo.Usuario
        fields = ('nombre','apellido_paterno', 'apellido_materno','correo',)
    
class ModificarPassword(forms.ModelForm):
    class Meta:
        model = modelo.Usuario
        fields = ('password',)

    def save(self, commit=True):
        usuario = super(ModificarPassword, self).save(commit=False)
        usuario.set_password(self.cleaned_data["password"])
        
        if commit:
            
            usuario.save()
        return usuario
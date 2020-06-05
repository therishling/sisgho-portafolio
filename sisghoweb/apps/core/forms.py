from django import forms
from django.contrib.auth.forms import ReadOnlyPasswordHashField, UserChangeForm
from apps.core import models as modelo


class HuespedForm(forms.ModelForm):
    class Meta:
        model = modelo.Huesped
        fields = ('nombre','apellidopaterno','apellidomaterno','rut','fechadesde','fechahasta','cliente')

class AsHabitacionForm(forms.ModelForm):
    class Meta:
        model = modelo.Huesped
        fields = ('habitacion',)
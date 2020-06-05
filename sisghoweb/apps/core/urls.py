
from django.contrib import admin
from django.urls import path, re_path
from django.contrib.auth.decorators import login_required
from apps.core import views as vista
urlpatterns = [
    #INDEX
    path('dashboard/', login_required(vista.Dashboard.as_view()) ,name='dashboard'),
    path('dashboard/reserva-habitacion', login_required(vista.ReservarHabitacion.as_view()) ,name='reservar habitacion'),
    re_path(r'^dashboard/reserva-habitacion/modificar-huesped/(?P<pk>\d+)/$', login_required(vista.ModificarHuesped.as_view()) ,name='modificar huesped'),
    re_path(r'^dashboard/reserva-habitacion/cancelar-reserva/(?P<pk>\d+)/$', login_required(vista.CancelarReserva.as_view()) ,name='cancelar reserva'),
    path('dashboard/asignar-habitacion', login_required(vista.SeleccionarHabitacion.as_view()) ,name='asignar habitacion'),
    re_path(r'^dashboard/asignar-habitacion/(?P<pk>\d+)/$', login_required(vista.AsignarHabitacion.as_view()) ,name='asignar habitacion huesped'),


]
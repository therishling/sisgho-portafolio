
from django.contrib import admin
from django.urls import path, re_path
from django.contrib.auth.decorators import login_required
from apps.core import views as vista
urlpatterns = [
    #INDEX
    path('', vista.Index.as_view() ,name='index'),
    #DASHBOARD
    path('dashboard/', login_required(vista.Dashboard.as_view()) ,name='dashboard'),
    #RESERVA HABITACION
    path('dashboard/reserva-habitacion', login_required(vista.ReservarHabitacion.as_view()) ,name='reservar habitacion'),
    re_path(r'^dashboard/reserva-habitacion/modificar-huesped/(?P<pk>\d+)/$', login_required(vista.ModificarHuesped.as_view()) ,name='modificar huesped'),
    re_path(r'^dashboard/reserva-habitacion/cancelar-reserva/(?P<pk>\d+)/$', login_required(vista.CancelarReserva.as_view()) ,name='cancelar reserva'),
    path('dashboard/asignar-habitacion', login_required(vista.SeleccionarHabitacion.as_view()) ,name='asignar habitacion'),
    re_path(r'^dashboard/asignar-habitacion/(?P<pk>\d+)/$', login_required(vista.AsignarHabitacion.as_view()) ,name='asignar habitacion huesped'),
    #SOLICITUD COMPRA / FACTURA
    path('dashboard/solicitud-compra', login_required(vista.SolicitudCompra.as_view()) ,name='nueva solicitud compra'),
    path('dashboard/emitir-factura', login_required(vista.ListarClientesFactura.as_view()) ,name='emitir factura'),
    re_path(r'^dashboard/emitir-factura/(?P<pk>\d+)/$', login_required(vista.EmitirFactura.as_view()) ,name='emitir factura form'),
    path('dashboard/listar-facturas-emitidas', login_required(vista.ListarFacturasEmitidas.as_view()) ,name='listar facturas emitidas'),
    re_path(r'^dashboard/pagar-factura/(?P<pk>\d+)/$', login_required(vista.PagoFactura.as_view()) ,name='pago factura'),
    re_path(r'^dashboard/detalle-pago/(?P<pk>\d+)/(?P<pk2>\d+)/$', login_required(vista.DetallePago.as_view()) ,name='detalle pago'),

]
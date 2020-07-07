
from django.contrib import admin
from django.urls import path, re_path
from django.contrib.auth.decorators import login_required
from apps.core import views as vista
from django.contrib.auth.views import PasswordChangeView, PasswordChangeDoneView
urlpatterns = [
    # INDEX
    path('', vista.Index.as_view(), name='index'),

    # DASHBOARD
    path('dashboard/', login_required(vista.Dashboard.as_view()), name='dashboard'),

    # RESERVA HABITACION
    path('dashboard/reserva-habitacion',
         login_required(vista.ReservarHabitacion.as_view()), name='reservar habitacion'),
         
    re_path(r'^dashboard/reserva-habitacion/modificar-huesped/(?P<pk>\d+)/$',
            login_required(vista.ModificarHuesped.as_view()), name='modificar huesped'),

    re_path(r'^dashboard/reserva-habitacion/cancelar-reserva/(?P<pk>\d+)/$',
            login_required(vista.CancelarReserva.as_view()), name='cancelar reserva'),

    path('dashboard/asignar-habitacion',
         login_required(vista.SeleccionarHabitacion.as_view()), name='asignar habitacion'),

    re_path(r'^dashboard/asignar-habitacion/(?P<pk>\d+)/$', login_required(
        vista.AsignarHabitacion.as_view()), name='asignar habitacion huesped'),

    # SOLICITUD COMPRA / FACTURA
    path('dashboard/solicitud-compra',
         login_required(vista.SolicitudCompra.as_view()), name='nueva solicitud compra'),

    path('dashboard/emitir-factura',
         login_required(vista.ListarClientesFactura.as_view()), name='emitir factura'),

    re_path(r'^dashboard/emitir-factura/(?P<pk>\d+)/$',
            login_required(vista.EmitirFactura.as_view()), name='emitir factura form'),

    path('dashboard/listar-facturas-emitidas', login_required(
        vista.ListarFacturasEmitidas.as_view()), name='listar facturas emitidas'),

    re_path(r'^dashboard/pagar-factura/(?P<pk>\d+)/$',
            login_required(vista.PagoFactura.as_view()), name='pago factura'),

    re_path(r'^dashboard/detalle-pago/(?P<pk>\d+)/(?P<pk2>\d+)/$',
            login_required(vista.DetallePago.as_view()), name='detalle pago'),

    # PDF
    re_path(r'^dashboard/factura-pdf/(?P<pk>\d+)/$',
            login_required(vista.FacturaPDF.as_view()), name='factura pdf'),

    

    # PEDIDO PRODUCTOS
    path('dashboard/listar-proveedor',
         login_required(vista.ListaProveedor.as_view()), name='listar proveedor'),

    re_path(r'^dashboard/solicitar-producto/(?P<pk>\d+)/$',
            login_required(vista.SolicitarProducto.as_view()), name='solicitar producto'),

    path('dashboard/pedidos',
         login_required(vista.ListarPedidos.as_view()), name='listar pedidos'),

    re_path(r'^dashboard/pedidos/(?P<pk>\d+)/$', login_required(
        vista.AdministrarSolicitud.as_view()), name='administrar solicitud'),

    path('dashboard/actualizar', login_required(vista.ActualizarEstHab.as_view()),
         name='actualizar estado habitacion'),

    # INFORMES Y ESTADISTICAS
    path('dashboard/estadisticas',
         login_required(vista.obtener_datos), name='estadisticas'),

    path('dashboard/informes',
         login_required(vista.Informes.as_view()), name='informes'),

    # USUARIO
    re_path(r'^dashboard/perfil/(?P<pk>\d+)/$',
            login_required(vista.ModificarPerfil.as_view()), name='actualizar perfil'),

    re_path(r'^dashboard/password/(?P<pk>\d+)/$', login_required(PasswordChangeView.as_view(
        template_name='dashboard/usuario/cambiarpass.html'
    )), name='actualizar password'),
    
    path('dashboard/password/done', login_required(PasswordChangeDoneView.as_view(
        template_name='dashboard/usuario/cambiarpass_done.html'
    )), name='password_change_done'),

    #FORMULARIO CONTACTO
    path('contacto',
         vista.Contacto.as_view(), name='contacto'),
]

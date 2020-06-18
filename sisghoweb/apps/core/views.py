from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect, HttpResponseBadRequest, JsonResponse
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, TemplateView, View, FormView
from django.views.generic.edit import ModelFormMixin
from django.urls import reverse, reverse_lazy
from apps.core import models as modelos
from apps.core import forms as formularios
from django.contrib.auth.mixins import UserPassesTestMixin, LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.db import connection
from datetime import date
from itertools import chain
from django.db.models import Q
from django.views.decorators.http import require_http_methods
from django.template import Context
from django.template.loader import get_template
from xhtml2pdf import pisa
# Create your views here.


class Index(TemplateView):
    template_name = 'index.html'


class Dashboard(TemplateView):
    template_name = 'dashboard/index.html'

   

# Registrar Huespedes


class ReservarHabitacion(UserPassesTestMixin, SuccessMessageMixin, CreateView):
    model = modelos.Huesped
    form_class = formularios.HuespedForm
    template_name = 'dashboard/cliente/reservahabitacion.html'
    success_message = 'Huesped agregado.'
    success_url = reverse_lazy('reservar habitacion')

    def test_func(self):
        user = self.request.user
        if user.tipousuario.idtipousuario == 3:
            return True

    def handle_no_permission(self):
        return redirect('dashboard')

    def get_context_data(self, **kwargs):
        context = super(ReservarHabitacion, self).get_context_data(**kwargs)
        context['huespedes'] = modelos.Huesped.objects.all()
        context['cliente'] = modelos.Cliente.objects.get(
            usuario=self.request.user.idusuario)
        context['time'] = date.today()
        return context


class ModificarHuesped(UserPassesTestMixin, SuccessMessageMixin, UpdateView):

    model = modelos.Huesped
    form_class = formularios.HuespedForm
    template_name = 'dashboard/cliente/reservahabitacion.html'
    success_message = 'Huesped modificado.'
    success_url = reverse_lazy('reservar habitacion')
    context_object_name = 'huesped'

    def test_func(self):
        user = self.request.user
        if user.tipousuario.idtipousuario == 3:
            return True

    def handle_no_permission(self):
        return redirect('dashboard')


class CancelarReserva(UserPassesTestMixin, SuccessMessageMixin, DeleteView):
    model = modelos.Huesped
    template_name = 'dashboard/cliente/reservahabitacion.html'
    success_message = 'Reserva Cancelada'
    success_url = reverse_lazy('reservar habitacion')
    context_object_name = 'huesped'

    def test_func(self):
        user = self.request.user
        if user.tipousuario.idtipousuario == 3:
            return True

    def handle_no_permission(self):
        return redirect('dashboard')


class SeleccionarHabitacion(UserPassesTestMixin, SuccessMessageMixin, CreateView):
    model = modelos.DetalleReserva
    form_class = formularios.DetalleReservaForm
    template_name = 'dashboard/empleado/asignarhabi.html'
    success_message = 'Habitacion asignada.'
    success_url = reverse_lazy('asignar habitacion')

    def test_func(self):
        user = self.request.user
        if user.tipousuario.idtipousuario == 2:
            return True

    def handle_no_permission(self):
        return redirect('dashboard')

    def get_context_data(self, **kwargs):
        context = super(SeleccionarHabitacion, self).get_context_data(**kwargs)
        context['huespedes'] = modelos.Huesped.objects.all().filter(fechahasta__gte = date.today()).order_by('idhuesped')
        context['habitaciones'] = modelos.Habitacion.objects.all().filter(
            estadohabitacion=1)
        return context

    def post(self, request, *args, **kwargs):
        habitacion = ""
        huesped = ""
        if self.request.method == 'POST':
            huesped = modelos.Huesped.objects.get(
                idhuesped=self.request.POST.get('huesped'))
            habitacion = modelos.Habitacion.objects.get(
                idhabitacion=self.request.POST.get('habitacion'))
            huesped.habitacion = habitacion
            huesped.save()
            if self.request.POST.get('habitacion'):
                habitacion = modelos.Habitacion.objects.get(
                    idhabitacion=self.request.POST.get('habitacion'))
                estadohabitacion = modelos.Estadohabitacion.objects.get(
                    idestado=2)
                habitacion.estadohabitacion = estadohabitacion
                habitacion.save()

        return super().post(request, *args, **kwargs)

    def form_valid(self, form):
        huesped = modelos.Huesped.objects.get(
            idhuesped=self.request.POST.get('huesped'))
        habitacion = modelos.Habitacion.objects.get(
            idhabitacion=self.request.POST.get('habitacion'))
        dias = huesped.fechahasta - huesped.fechadesde
        total = dias.days * habitacion.precio
        self.object = form.save(commit=False)
        self.object.huesped = huesped
        self.object.dias = dias.days
        self.object.total = total
        self.object.habitacion = habitacion
        self.object = form.save()
        # Llamado a procedimiento almacenado
        with connection.cursor() as cursor:
            cursor.callproc('p_actualizar_habitaciones')
        return super(SeleccionarHabitacion, self).form_valid(form)


class AsignarHabitacion(UserPassesTestMixin, SuccessMessageMixin, UpdateView):
    model = modelos.Huesped
    form_class = formularios.AsHabitacionForm
    template_name = 'dashboard/empleado/asignarhabi.html'
    success_message = 'Habitacion asignada.'
    success_url = reverse_lazy('asignar habitacion')
    context_object_name = 'habitacion'

    def post(self, request, *args, **kwargs):
        huesped = modelos.Huesped.objects.get(
            idhuesped=self.request.POST.get('huesped'))
        habitacion = modelos.Habitacion.objects.get(
            idhabitacion=self.request.POST.get('habitacion'))
        dias = huesped.fechahasta - huesped.fechadesde
        total = dias.days * habitacion.precio
        detallereserva = modelos.DetalleReserva.objects.get(huesped=huesped)
        if self.request.method == 'POST':
            if self.request.POST.get('habitacion'):
                estadohabitacion = modelos.Estadohabitacion.objects.get(
                    idestado=2)
                habitacion.estadohabitacion = estadohabitacion
                detallereserva.habitacion = habitacion
                detallereserva.total = total
                detallereserva.save()
                habitacion.save()

        return super().post(request, *args, **kwargs)

    def form_valid(self, form):

        self.object = form.save()
        # Llamado a procedimiento almacenado
        with connection.cursor() as cursor:
            cursor.callproc('p_actualizar_habitaciones')
        return super(AsignarHabitacion, self).form_valid(form)

    def test_func(self):
        user = self.request.user
        if user.tipousuario.idtipousuario == 2:
            return True

    def handle_no_permission(self):
        return redirect('dashboard')


# VISTAS SOLICITUD DE COMPRA
class SolicitudCompra(UserPassesTestMixin, SuccessMessageMixin, CreateView):
    model = modelos.SolicitudCompra
    form_class = formularios.SolicitudCompraForm
    template_name = 'dashboard/empleado/solicitudcompra.html'
    success_message = 'Solicitud emitida.'
    success_url = reverse_lazy('nueva solicitud compra')

    def test_func(self):
        user = self.request.user
        if user.tipousuario.idtipousuario == 2:
            return True

    def handle_no_permission(self):
        return redirect('dashboard')

    def get_context_data(self, **kwargs):
        context = super(SolicitudCompra, self).get_context_data(**kwargs)
        context['huespedes'] = modelos.Huesped.objects.all().filter(
            habitacion__isnull=False, fechahasta__gte = date.today()).order_by('idhuesped')
        context['servicios'] = modelos.Serviciocomedor.objects.all()
        return context

    def form_valid(self, form):
        huesped = modelos.Huesped.objects.get(
            idhuesped=self.request.POST.get('huesped'))
        servicio = modelos.Serviciocomedor.objects.get(
            idservicio=self.request.POST.get('servicio'))
        self.object = form.save(commit=False)
        self.object.fecha = date.today()
        self.object.huesped = huesped
        self.object.serviciocomedor = servicio
        self.object = form.save()
        return super(SolicitudCompra, self).form_valid(form)


class ListarClientesFactura(UserPassesTestMixin, SuccessMessageMixin, ListView):
    model = modelos.Factura
    template_name = 'dashboard/empleado/emitirfactura.html'

    def test_func(self):
        user = self.request.user
        if user.tipousuario.idtipousuario == 2:
            return True

    def handle_no_permission(self):
        return redirect('dashboard')

    def get_context_data(self, **kwargs):

        huespedes = modelos.Huesped.objects.values_list(
            'idhuesped', flat=True).filter(habitacion__isnull=False)
        facturas = modelos.Detallefactura.objects.all().values_list('huesped', flat=True)

        facturascompras = modelos.Detallefactura.objects.all(
        ).values_list('solicitudcompra', flat=True)
        solicitudcompraid = modelos.SolicitudCompra.objects.all(
        ).values_list('idsolicitud', flat=True)

        q = huespedes.difference(facturas)
        q2 = solicitudcompraid.difference(facturascompras)
        q3 = modelos.SolicitudCompra.objects.all().values_list(
            'huesped', flat=True).filter(idsolicitud__in=q2)
        idclientes = modelos.Huesped.objects.all().values_list(
            'cliente', flat=True).filter(Q(idhuesped__in=q) | Q(idhuesped__in=q3))
        clientes = modelos.Cliente.objects.all().filter(idcliente__in=idclientes)
        context = super(ListarClientesFactura, self).get_context_data(**kwargs)
        context['clientes'] = clientes
        return context


class EmitirFactura(UserPassesTestMixin, SuccessMessageMixin, CreateView):
    model = modelos.Factura
    form_class = formularios.FacturaForm
    template_name = 'dashboard/empleado/emitirfacturaform.html'
    success_message = 'Factura emitida.'
    success_url = reverse_lazy('emitir factura')

    def test_func(self):
        user = self.request.user
        if user.tipousuario.idtipousuario == 2:
            return True

    def handle_no_permission(self):
        return redirect('dashboard')

    def get_context_data(self, **kwargs):
        huespedes = modelos.Huesped.objects.values_list('idhuesped', flat=True).filter(
            habitacion__isnull=False, cliente=self.kwargs['pk'])
        facturas = modelos.Detallefactura.objects.all().values_list('huesped', flat=True)

        q = huespedes.difference(facturas)
        detallereserva = modelos.DetalleReserva.objects.all().filter(huesped__in=q)
        facturassolicitud = modelos.Detallefactura.objects.all(
        ).values_list('solicitudcompra', flat=True)
        solicitudcompraid = modelos.SolicitudCompra.objects.all(
        ).values_list('idsolicitud').filter(huesped__in=huespedes)

        q2 = solicitudcompraid.difference(facturassolicitud)

        solicitudcompra = modelos.SolicitudCompra.objects.all().filter(idsolicitud__in=q2)

        context = super(EmitirFactura, self).get_context_data(**kwargs)
        context['detallesreservas'] = detallereserva
        context['solicitudescompras'] = solicitudcompra
        return context

    def form_valid(self, form, **kwargs):
        reservas = self.request.POST.getlist('chkreserva[]')
        servicios = self.request.POST.getlist('chkservicio[]')
        clienteid = self.kwargs['pk']
        cliente = modelos.Cliente.objects.get(idcliente=clienteid)
        estadofactura = modelos.Estadofactura.objects.get(idestado=1)

        self.object = form.save(commit=False)
        self.object.giro = 'Hostal Doña Clarita'
        self.object.fechafactura = date.today()
        self.object.cliente = cliente
        self.object.estadofactura = estadofactura
        self.object = form.save()

        for reservaid in reservas:
            reserva = modelos.DetalleReserva.objects.get(idreserva=reservaid)

            detallefact = modelos.Detallefactura()
            detallefact.total = reserva.total
            detallefact.factura = self.object
            detallefact.huesped = reserva.huesped
            detallefact.detallereserva = reserva
            detallefact.save()

        for solicitudid in servicios:
            servicio = modelos.SolicitudCompra.objects.get(
                idsolicitud=solicitudid)

            detallefact = modelos.Detallefactura()
            detallefact.total = servicio.serviciocomedor.precio * servicio.cantidad
            detallefact.factura = self.object
            detallefact.huesped = servicio.huesped
            detallefact.solicitudcompra = servicio
            detallefact.save()

        print(self.object.idfactura)
        return super(EmitirFactura, self).form_valid(form)


class ListarFacturasEmitidas(UserPassesTestMixin, TemplateView):
    template_name = 'dashboard/cliente/listafacturas.html'

    def test_func(self):
        user = self.request.user
        if user.tipousuario.idtipousuario == 3 or user.tipousuario.idtipousuario == 2:
            return True

    def handle_no_permission(self):
        return redirect('dashboard')

    def get_context_data(self, **kwargs):
        if self.request.user.tipousuario.idtipousuario == 3:
            cliente = modelos.Cliente.objects.get(
                usuario=self.request.user.idusuario)
            facturas = modelos.Factura.objects.all().filter(cliente=cliente.idcliente).order_by('idfactura')
            facturasid = modelos.Factura.objects.values_list(
                'idfactura', flat=True).filter(cliente=cliente.idcliente).order_by('idfactura')
        else:
            cliente = modelos.Cliente.objects.all().values_list('idcliente', flat=True)
            facturas = modelos.Factura.objects.all().filter(cliente__in=cliente).order_by('idfactura')
            facturasid = modelos.Factura.objects.values_list(
                'idfactura', flat=True).filter(cliente__in=cliente).order_by('idfactura')

        detallefactura = modelos.Detallefactura.objects.all().filter(factura__in=facturasid).order_by('iddetalle')

        context = super(ListarFacturasEmitidas,
                        self).get_context_data(**kwargs)
        context['facturas'] = facturas
        context['detalles'] = detallefactura
        return context


class PagoFactura(UserPassesTestMixin, SuccessMessageMixin, UpdateView):

    model = modelos.Factura
    form_class = formularios.FacturaForm
    template_name = 'dashboard/cliente/mediodepago.html'
    success_message = 'Pago confirmado'
    context_object_name = 'factura'

    def test_func(self):
        user = self.request.user
        if user.tipousuario.idtipousuario == 3 or user.tipousuario.idtipousuario == 2:
            return True

    def handle_no_permission(self):
        return redirect('dashboard')

    def post(self, request, *args, **kwargs):
        if self.request.method == 'POST':
            if self.request.user.tipousuario.idtipousuario == 3:
                options = int(self.request.POST.get('options'))

                estadofactura = modelos.Estadofactura.objects.get(
                    idestado=options)
            else:
                estadofactura = modelos.Estadofactura.objects.get(idestado=2)
            factura = modelos.Factura.objects.get(idfactura=self.kwargs['pk'])
            factura.estadofactura = estadofactura
            factura.fechapago = date.today()
            factura.save()

        return super().post(request, *args, **kwargs)

    def get_success_url(self, **kwargs):
        idfact = int(self.kwargs['pk'])
        factura = modelos.Factura.objects.get(idfactura=idfact)
        if self.request.user.tipousuario.idtipousuario == 3:
            return reverse_lazy('detalle pago', kwargs={'pk': factura.estadofactura.idestado, 'pk2': factura.idfactura})
        else:
            return reverse_lazy('listar facturas emitidas')


class DetallePago(UserPassesTestMixin, SuccessMessageMixin, TemplateView):
    template_name = 'dashboard/cliente/detalledelpago.html'

    def test_func(self):
        user = self.request.user
        if user.tipousuario.idtipousuario == 3:
            return True

    def handle_no_permission(self):
        return redirect('dashboard')

    def get_context_data(self, **kwargs):
        factura = modelos.Factura.objects.get(
            idfactura=int(self.kwargs['pk2']))
        detallefact = modelos.Detallefactura.objects.all().filter(factura=factura)
        total = 0
        for detalle in detallefact:
            total = total + detalle.total
        context = super(DetallePago, self).get_context_data(**kwargs)
        context['option'] = int(self.kwargs['pk'])
        context['total'] = total
        return context
# PDF


class FacturaPDF(View):

    def get(self, request, *args, **kwargs):
        template = get_template('pdf/factura.html')
        factura = modelos.Factura.objects.get(idfactura=self.kwargs['pk'])
        detallefactura = modelos.Detallefactura.objects.all().filter(factura=factura)
        usuario = self.request.user
        subtotal = 0
        for d in detallefactura:
            subtotal = subtotal + d.total
        iva = round(subtotal * 0.19)

        if factura.cliente.usuario.idusuario == usuario.idusuario:

            context = {
                'factura': factura,
                'detallefactura': detallefactura,
                'subtotal': subtotal,
                'iva': iva,
                'total': subtotal + iva
            }
            html = template.render(context)
            response = HttpResponse(content_type="application/pdf")
            response['Content-Disposition'] = 'attachment; filename=' + \
                "factura-numero-" + self.kwargs['pk'] + ".pdf"
            pisaStatus = pisa.CreatePDF(
                html, dest=response)

            

            if pisaStatus.err:
                return HttpResponse('error')
            return response
        else:
            return redirect('listar facturas emitidas')


# PEDIDOS
class ListaProveedor(UserPassesTestMixin, TemplateView):
    template_name = 'dashboard/empleado/solicitarprod.html'

    def test_func(self):
        user = self.request.user
        if user.tipousuario.idtipousuario == 2:
            return True

    def handle_no_permission(self):
        return redirect('dashboard')

    def get_context_data(self, **kwargs):

        context = super(ListaProveedor, self).get_context_data(**kwargs)
        context['proveedores'] = modelos.Proveedor.objects.all().order_by('idproveedor')
        return context


class SolicitarProducto(UserPassesTestMixin, SuccessMessageMixin, CreateView):
    model = modelos.Pedido
    form_class = formularios.PedidoForm
    template_name = 'dashboard/empleado/seleccionarprod.html'
    success_message = 'Productos solicitados.'
    success_url = reverse_lazy('listar proveedor')

    def test_func(self):
        user = self.request.user
        if user.tipousuario.idtipousuario == 2:
            return True

    def handle_no_permission(self):
        return redirect('dashboard')

    def get_context_data(self, **kwargs):
        productos = modelos.Producto.objects.all().filter(
            proveedor=self.kwargs['pk'])

        context = super(SolicitarProducto, self).get_context_data(**kwargs)
        context['productos'] = productos
        return context

    def form_valid(self, form, **kwargs):
        cantidad = self.request.POST.getlist('cantidad[]')
        idprod = self.request.POST.getlist('idpro[]')
        arr = []
        cont = 0
        for c in idprod:
            arr.append([c, cantidad[cont]])
            cont = cont+1

        proveedorid = self.kwargs['pk']
        emp = modelos.Empleado.objects.get(usuario=self.request.user.idusuario)

        estadopedido = modelos.Estadopedido.objects.get(idestado=1)

        self.object = form.save(commit=False)
        self.object.observaciones = self.request.POST.get('observaciones')
        self.object.fechapedido = date.today()
        self.object.empleado = emp
        self.object.estadopedido = estadopedido
        self.object.proveedor = modelos.Proveedor.objects.get(
            idproveedor=proveedorid)
        self.object = form.save()

        for pedido in arr:
            if int(pedido[1]) > 0:
                producto = modelos.Producto.objects.get(
                    idproducto=int(pedido[0]))
                detallepedido = modelos.Detallepedido()
                detallepedido.cantidad = int(pedido[1])
                detallepedido.total = int(pedido[1])*producto.precio
                detallepedido.pedido = self.object
                detallepedido.producto = producto
                detallepedido.save()
        return super(SolicitarProducto, self).form_valid(form)


class ListarPedidos(UserPassesTestMixin, SuccessMessageMixin, ListView):

    model = modelos.Pedido
    template_name = 'dashboard/empleado/solicitudes.html'
    context_object_name = 'pedido'

    def test_func(self):
        user = self.request.user
        if user.tipousuario.idtipousuario == 2 or user.tipousuario.idtipousuario == 4:
            return True

    def handle_no_permission(self):
        return redirect('dashboard')

    def get_context_data(self, **kwargs):
        if self.request.user.tipousuario.idtipousuario == 2:

            pedidos = modelos.Pedido.objects.all().order_by('idpedido')
        if self.request.user.tipousuario.idtipousuario == 4:
            proveedor = modelos.Proveedor.objects.get(
                usuario=self.request.user.idusuario)
            pedidos = modelos.Pedido.objects.all().filter(proveedor=proveedor.idproveedor).order_by('idpedido')

        context = super(ListarPedidos, self).get_context_data(**kwargs)
        context['pedidos'] = pedidos
        context['detalles'] = modelos.Detallepedido.objects.all()
        return context


class AdministrarSolicitud(UserPassesTestMixin, SuccessMessageMixin, UpdateView):

    model = modelos.Pedido
    form_class = formularios.PedidoForm
    template_name = 'dashboard/empleado/solicitudes.html'
    success_message = 'Solicitud Actualizada'
    context_object_name = 'pedido'
    success_url = reverse_lazy('listar pedidos')

    def test_func(self):
        user = self.request.user
        if user.tipousuario.idtipousuario == 2 or user.tipousuario.idtipousuario == 4:
            return True

    def handle_no_permission(self):
        return redirect('dashboard')

    def post(self, request, *args, **kwargs):

        if self.request.method == 'POST':
            pedido = modelos.Pedido.objects.get(idpedido=self.kwargs['pk'])
            if 'rechazar' in self.request.POST:
                estadopedido = modelos.Estadopedido.objects.get(idestado=4)

            if 'aceptar' in self.request.POST and self.request.user.tipousuario.idtipousuario == 4:
                estadopedido = modelos.Estadopedido.objects.get(idestado=2)
            if 'recibir' in self.request.POST and self.request.user.tipousuario.idtipousuario == 2:
                estadopedido = modelos.Estadopedido.objects.get(idestado=3)
                detallepedido = modelos.Detallepedido.objects.all().filter(pedido=pedido.idpedido)
                for dp in detallepedido:
                    producto = modelos.Producto.objects.get(
                        idproducto=dp.producto.idproducto)
                    producto.stock = producto.stock + dp.cantidad
                    producto.save()
            pedido.estadopedido = estadopedido
            pedido.save()
        return super().post(request, *args, **kwargs)

# ACTUALIZAR ESTADO HABITACIONES
class ActualizarEstHab(UserPassesTestMixin, SuccessMessageMixin, FormView):
    form_class = formularios.HabitacionForm
    template_name = 'dashboard/empleado/asignarhabi.html'
    success_message = 'Se actualizo el estado de las habitaciones.'
    success_url = reverse_lazy('asignar habitacion')

    def test_func(self):
        user = self.request.user
        if user.tipousuario.idtipousuario == 2 or user.tipousuario.idtipousuario == 4:
            return True

    def handle_no_permission(self):
        return redirect('dashboard')

    
    def form_valid(self, form):

        form.actualizar_estado()
        return super(ActualizarEstHab, self).form_valid(form)

#ESTADISTICAS
def obtener_datos(request, *args, **kwargs):
    
    #USUARIO CLIENTE
    if request.user.tipousuario.idtipousuario == 3:
        #DATOS DEL USUARIO
        cliente = modelos.Cliente.objects.get(usuario = request.user.idusuario)
        tipousuario = request.user.tipousuario.idtipousuario
        #ESTADISTICAS RESERVA
        #TOTAL RESERVAS FINALIZADAS
        reservasfinalizadas = len(modelos.Huesped.objects.all().filter(cliente = cliente.idcliente, fechahasta__lte = date.today()))
        #TOTALRESERVAS ACTIVAS
        reservasactivas = len(modelos.Huesped.objects.all().filter(cliente = cliente.idcliente, fechahasta__gte = date.today()))
        total_reservas = reservasfinalizadas + reservasactivas
        # ARRAYS CON LOS DATOS Y LABELS
        data_reserva = []
        data_reserva.append(reservasfinalizadas)
        data_reserva.append(reservasactivas)
        labels_reserva = []
        labels_reserva.append("Reservas Finalizadas")
        labels_reserva.append("Reservas Activas")

        #ESTADISTICAS FACTURA
        labels_factura = []
        labels_factura.append("Pagadas")
        labels_factura.append("En Proceso")
        labels_factura.append("No Pagadas")
        data_factura = []
        # TOTAL DE FACTURAS CON PAGOS CONFIRMADOS
        facturas_pagadas = len(modelos.Factura.objects.all().filter(cliente = cliente.idcliente, estadofactura = 2))
        # TOTAL FACTURAS EMITIDAS Y NO PAGADAS
        facturas_no_pagadas = len(modelos.Factura.objects.all().filter(cliente = cliente.idcliente, estadofactura = 1))
        # TOTAL FACTURAS EN PROCESO DE PAGO       
        facturas_en_proceso = len(modelos.Factura.objects.all().filter(cliente = cliente.idcliente, estadofactura__in = (3,4)))
        data_factura.append(facturas_pagadas)
        data_factura.append(facturas_en_proceso)
        data_factura.append(facturas_no_pagadas)
        # FACTURAS TOTALES
        facturas_totales = facturas_no_pagadas + facturas_en_proceso + facturas_pagadas
        

        
        # JSON    
        data = {
            
                "labels_reserva" : labels_reserva,
                "data_reserva": data_reserva,
                "tipousuario": tipousuario,
                "total_reserva": total_reservas,
                "labels_factura" : labels_factura,
                "data_factura" : data_factura,
                "total_factura" : facturas_totales
            
        }
        return JsonResponse(data)
    return HttpResponse("NO DATA")
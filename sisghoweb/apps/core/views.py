from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect, HttpResponseBadRequest
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, TemplateView
from django.views.generic.edit import ModelFormMixin
from django.urls import reverse,reverse_lazy
from apps.core import models as modelos
from apps.core import forms as formularios
from django.contrib.auth.mixins import UserPassesTestMixin, LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.db import connection
from datetime import date
from itertools import chain
from django.db.models import Q
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

    def get_context_data(self,**kwargs):
        context = super(ReservarHabitacion,self).get_context_data(**kwargs)
        context['huespedes'] = modelos.Huesped.objects.all()
        context['cliente'] = modelos.Cliente.objects.get(usuario = self.request.user.idusuario)
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

    def get_context_data(self,**kwargs):
        context = super(SeleccionarHabitacion,self).get_context_data(**kwargs)
        context['huespedes'] = modelos.Huesped.objects.all()
        context['habitaciones'] = modelos.Habitacion.objects.all().filter(estadohabitacion = 1)
        return context

    def post(self, request, *args, **kwargs):
        habitacion = ""
        huesped = ""
        if self.request.method == 'POST':
            huesped = modelos.Huesped.objects.get(idhuesped=self.request.POST.get('huesped'))
            habitacion = modelos.Habitacion.objects.get(idhabitacion=self.request.POST.get('habitacion'))
            huesped.habitacion = habitacion
            huesped.save()
            if self.request.POST.get('habitacion'):
                habitacion = modelos.Habitacion.objects.get(idhabitacion=self.request.POST.get('habitacion'))
                estadohabitacion = modelos.Estadohabitacion.objects.get(idestado = 2)
                habitacion.estadohabitacion = estadohabitacion
                habitacion.save()
         
        return super().post(request, *args, **kwargs)

    def form_valid(self,form):
        huesped = modelos.Huesped.objects.get(idhuesped=self.request.POST.get('huesped'))
        habitacion = modelos.Habitacion.objects.get(idhabitacion=self.request.POST.get('habitacion'))
        dias = huesped.fechahasta - huesped.fechadesde
        total = dias.days * habitacion.precio
        self.object = form.save(commit = False)
        self.object.huesped = huesped
        self.object.dias = dias.days
        self.object.total = total
        self.object.habitacion = habitacion
        self.object = form.save()
        #Llamado a procedimiento almacenado
        with connection.cursor() as cursor:
            cursor.callproc('p_actualizar_habitaciones')
        return super(SeleccionarHabitacion,self).form_valid(form)

class AsignarHabitacion(UserPassesTestMixin, SuccessMessageMixin, UpdateView):
    model = modelos.Huesped
    form_class = formularios.AsHabitacionForm
    template_name = 'dashboard/empleado/asignarhabi.html'
    success_message = 'Habitacion asignada.'
    success_url = reverse_lazy('asignar habitacion')
    context_object_name = 'habitacion'
    
    def post(self, request, *args, **kwargs):
        huesped = modelos.Huesped.objects.get(idhuesped=self.request.POST.get('huesped'))
        habitacion = modelos.Habitacion.objects.get(idhabitacion=self.request.POST.get('habitacion'))
        dias = huesped.fechahasta - huesped.fechadesde
        total = dias.days * habitacion.precio
        detallereserva = modelos.DetalleReserva.objects.get(huesped=huesped)
        if self.request.method == 'POST':
            if self.request.POST.get('habitacion'):
                estadohabitacion = modelos.Estadohabitacion.objects.get(idestado = 2)
                habitacion.estadohabitacion = estadohabitacion
                detallereserva.habitacion = habitacion
                detallereserva.total = total
                detallereserva.save()
                habitacion.save()
                
                
            
        return super().post(request, *args, **kwargs)
    
    def form_valid(self,form):

        self.object = form.save()
        #Llamado a procedimiento almacenado
        with connection.cursor() as cursor:
            cursor.callproc('p_actualizar_habitaciones')
        return super(AsignarHabitacion,self).form_valid(form)
        
    

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

    def get_context_data(self,**kwargs):
        context = super(SolicitudCompra,self).get_context_data(**kwargs)
        context['huespedes'] = modelos.Huesped.objects.all().filter(habitacion__isnull = False)
        context['servicios'] = modelos.Serviciocomedor.objects.all() 
        return context
    
    def form_valid(self,form):
        huesped = modelos.Huesped.objects.get(idhuesped=self.request.POST.get('huesped'))
        servicio = modelos.Serviciocomedor.objects.get(idservicio=self.request.POST.get('servicio'))
        self.object = form.save(commit=False)
        self.object.fecha = date.today()
        self.object.huesped = huesped
        self.object.serviciocomedor = servicio
        self.object = form.save()
        return super(SolicitudCompra,self).form_valid(form)


class ListarClientesFactura(UserPassesTestMixin, SuccessMessageMixin, ListView):
    model = modelos.Factura
    template_name = 'dashboard/empleado/emitirfactura.html'

    def test_func(self):
        user = self.request.user
        if user.tipousuario.idtipousuario == 2:
            return True
    
    def handle_no_permission(self):
        return redirect('dashboard')

    def get_context_data(self,**kwargs):
        
        huespedes = modelos.Huesped.objects.values_list('idhuesped',flat=True).filter(habitacion__isnull = False)
        facturas = modelos.Detallefactura.objects.all().values_list('huesped',flat=True )

        facturascompras = modelos.Detallefactura.objects.all().values_list('solicitudcompra',flat=True )
        solicitudcompraid = modelos.SolicitudCompra.objects.all().values_list('idsolicitud', flat = True)

        
        q = huespedes.difference(facturas)
        q2 = solicitudcompraid.difference(facturascompras)
        q3 = modelos.SolicitudCompra.objects.all().values_list('huesped', flat = True).filter(idsolicitud__in=q2)
        idclientes = modelos.Huesped.objects.all().values_list('cliente', flat=True).filter(Q(idhuesped__in=q) | Q(idhuesped__in=q3))
        clientes = modelos.Cliente.objects.all().filter(idcliente__in=idclientes)
        context = super(ListarClientesFactura,self).get_context_data(**kwargs)
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

    def get_context_data(self,**kwargs):
        huespedes = modelos.Huesped.objects.values_list('idhuesped',flat=True).filter(habitacion__isnull = False, cliente = self.kwargs['pk'])
        facturas = modelos.Detallefactura.objects.all().values_list('huesped',flat=True )
        
        q = huespedes.difference(facturas)
        detallereserva =  modelos.DetalleReserva.objects.all().filter(huesped__in=q)
        facturassolicitud = modelos.Detallefactura.objects.all().values_list('solicitudcompra',flat=True )
        solicitudcompraid = modelos.SolicitudCompra.objects.all().values_list('idsolicitud').filter(huesped__in = huespedes)
        
        q2 = solicitudcompraid.difference(facturassolicitud)

        solicitudcompra = modelos.SolicitudCompra.objects.all().filter(idsolicitud__in = q2)

        context = super(EmitirFactura,self).get_context_data(**kwargs)
        context['detallesreservas'] = detallereserva
        context['solicitudescompras'] = solicitudcompra
        return context
    
    def form_valid(self,form, **kwargs):
        reservas = self.request.POST.getlist('chkreserva[]')
        servicios = self.request.POST.getlist('chkservicio[]')
        clienteid = self.kwargs['pk']
        cliente = modelos.Cliente.objects.get(idcliente = clienteid)
        estadofactura = modelos.Estadofactura.objects.get(idestado = 1)

        self.object = form.save(commit=False)
        self.object.giro = 'Hostal Doña Clarita'
        self.object.fechafactura = date.today()
        self.object.cliente = cliente
        self.object.estadofactura = estadofactura
        self.object = form.save()

        for reservaid in reservas:
            reserva = modelos.DetalleReserva.objects.get(idreserva = reservaid)

            detallefact = modelos.Detallefactura()
            detallefact.total = reserva.total
            detallefact.factura = self.object
            detallefact.huesped = reserva.huesped
            detallefact.detallereserva = reserva
            detallefact.save()

        for solicitudid in servicios:
            servicio = modelos.SolicitudCompra.objects.get(idsolicitud = solicitudid)

            detallefact = modelos.Detallefactura()
            detallefact.total = servicio.serviciocomedor.precio * servicio.cantidad
            detallefact.factura = self.object
            detallefact.huesped = servicio.huesped
            detallefact.solicitudcompra = servicio
            detallefact.save()

        print(self.object.idfactura)
        return super(EmitirFactura,self).form_valid(form)
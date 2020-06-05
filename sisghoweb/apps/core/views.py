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
# Create your views here.
class Index(TemplateView):
    template_name = 'dashboard/index.html'


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
    model = modelos.Huesped
    form_class = formularios.AsHabitacionForm
    template_name = 'dashboard/empleado/asignarhabi.html'
    success_message = ''
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

class AsignarHabitacion(UserPassesTestMixin, SuccessMessageMixin, UpdateView):
    model = modelos.Huesped
    form_class = formularios.AsHabitacionForm
    template_name = 'dashboard/empleado/asignarhabi.html'
    success_message = 'Habitacion asignada.'
    success_url = reverse_lazy('asignar habitacion')
    context_object_name = 'habitacion'
    
    def post(self, request, *args, **kwargs):
        habitacion = ""
        if self.request.method == 'POST':
            if self.request.POST.get('habitacion'):
                habitacion = modelos.Habitacion.objects.get(idhabitacion=self.request.POST.get('habitacion'))
                estadohabitacion = modelos.Estadohabitacion.objects.get(idestado = 2)
                habitacion.estadohabitacion = estadohabitacion
                habitacion.save()
                
                
            
        return super().post(request, *args, **kwargs)
    
    def form_valid(self,form):

        self.object = form.save()
        with connection.cursor() as cursor:
            cursor.callproc('p_actualizar_habitaciones')
        return super(AsignarHabitacion,self).form_valid(form)
        
    

    def test_func(self):
        user = self.request.user
        if user.tipousuario.idtipousuario == 2:
            return True
    
    def handle_no_permission(self):
        return redirect('dashboard')

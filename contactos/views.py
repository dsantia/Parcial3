from django.shortcuts import render
from django.views import generic
from .models import Departamento, Telefono, Inscrito, Responsable, Contacto
from django.urls import reverse, reverse_lazy
from django.shortcuts import redirect
from django.contrib.admin.views.decorators import staff_member_required
from django.utils.decorators import method_decorator


class StaffRequiredMixin(object):

    @method_decorator(staff_member_required)
    def dispatch(self, request, *args, **kwargs):
        return super(StaffRequiredMixin, self).dispatch(request, *args, **kwargs)

# Create your views here.   
class DepartamentoListView(generic.ListView):
    model = Departamento
    template_name = "lista.html"

class DepartamentoDetailView(generic.DetailView):
    model = Departamento
    template_name = "detalle.html"

@method_decorator(staff_member_required, name='dispatch')
class DepartamentoCreateView(generic.CreateView):
    model = Departamento
    fields = '__all__'
    template_name = "nuevo.html"
    success_url = reverse_lazy('contactos:ListaDepartamento')

@method_decorator(staff_member_required, name='dispatch')
class DepartamentoUpdateView(generic.UpdateView):
    model = Departamento
    fields = '__all__'
    template_name = "editar.html"

    def get_success_url(self):
        return reverse_lazy('contactos:EditarDepartamento', args=[self.object.id]) + '?ok'

@method_decorator(staff_member_required, name='dispatch')
class DepartamentoDeleteView(generic.DeleteView):
    model = Departamento
    template_name = "borrar.html"
    success_url = reverse_lazy('contactos:ListaDepartamento')

# Telefono

class TelefonoListView(generic.ListView):
    model = Telefono
    template_name = "Telefonolista.html"

class TelefonoDetailView(generic.DetailView):
    model = Telefono
    template_name = "Telefonodetalle.html"

@method_decorator(staff_member_required, name='dispatch')
class TelefonoCreateView(generic.CreateView):
    model = Telefono
    fields = '__all__'
    template_name = "Telefononuevo.html"
    success_url = reverse_lazy('contactos:ListaTelefono')

@method_decorator(staff_member_required, name='dispatch')
class TelefonoUpdateView(generic.UpdateView):
    model = Telefono
    fields = '__all__'
    template_name = "Telefonoeditar.html"

    def get_success_url(self):
        return reverse_lazy('contactos:EditarTelefono', args=[self.object.id]) + '?ok'

@method_decorator(staff_member_required, name='dispatch')
class TelefonoDeleteView(generic.DeleteView):
    model = Telefono
    template_name = "Telefonoborrar.html"
    success_url = reverse_lazy('contactos:ListaTelefono')

#Inscrito

class InscritoListView(generic.ListView):
    model = Inscrito
    template_name = "Inscritolista.html"

class InscritoDetailView(generic.DetailView):
    model = Inscrito
    template_name = "Inscritodetalle.html"

@method_decorator(staff_member_required, name='dispatch')
class InscritoCreateView(generic.CreateView):
    model = Inscrito
    fields = '__all__'
    template_name = "Inscritonuevo.html"
    success_url = reverse_lazy('contactos:ListaInscrito')

@method_decorator(staff_member_required, name='dispatch')
class InscritoUpdateView(generic.UpdateView):
    model = Inscrito
    fields = '__all__'
    template_name = "Inscritoeditar.html"

    def get_success_url(self):
        return reverse_lazy('contactos:EditarInscrito', args=[self.object.id]) + '?ok'

@method_decorator(staff_member_required, name='dispatch')
class InscritoDeleteView(generic.DeleteView):
    model = Inscrito
    template_name = "Inscritoborrar.html"
    success_url = reverse_lazy('contactos:ListaInscrito')

    #Responsable

class ResponsableListView(generic.ListView):
    model = Responsable
    template_name = "Responsablelista.html"

class ResponsableDetailView(generic.DetailView):
    model = Responsable
    template_name = "Responsabledetalle.html"

@method_decorator(staff_member_required, name='dispatch')
class ResponsableCreateView(generic.CreateView):
    model = Responsable
    fields = '__all__'
    template_name = "Responsablenuevo.html"
    success_url = reverse_lazy('contactos:ListaResponsable')

@method_decorator(staff_member_required, name='dispatch')
class ResponsableUpdateView(generic.UpdateView):
    model = Responsable
    fields = '__all__'
    template_name = "Responsableeditar.html"

    def get_success_url(self):
        return reverse_lazy('contactos:EditarResponsable', args=[self.object.id]) + '?ok'

@method_decorator(staff_member_required, name='dispatch')
class ResponsableDeleteView(generic.DeleteView):
    model = Responsable
    template_name = "Responsableborrar.html"
    success_url = reverse_lazy('contactos:ListaResponsable')

#Contacto

class ContactoListView(generic.ListView):
    model = Contacto
    template_name = "Contactolista.html"

class ContactoDetailView(generic.DetailView):
    model = Contacto
    template_name = "Contactodetalle.html"

@method_decorator(staff_member_required, name='dispatch')
class ContactoCreateView(generic.CreateView):
    model = Contacto
    fields = '__all__'
    template_name = "Contactonuevo.html"
    success_url = reverse_lazy('contactos:ListaContacto')

@method_decorator(staff_member_required, name='dispatch')
class ContactoUpdateView(generic.UpdateView):
    model = Contacto
    fields = '__all__'
    template_name = "Contactoeditar.html"

    def get_success_url(self):
        return reverse_lazy('contactos:EditarContacto', args=[self.object.id]) + '?ok'

@method_decorator(staff_member_required, name='dispatch')
class ContactoDeleteView(generic.DeleteView):
    model = Contacto
    template_name = "Contactoborrar.html"
    success_url = reverse_lazy('contactos:ListaContacto')
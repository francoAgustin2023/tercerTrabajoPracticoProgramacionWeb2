from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.forms import UserCreationForm
from django.views.generic import CreateView, DeleteView, UpdateView, ListView, DetailView
from post.models import Publicacion
from django.db.models.query import QuerySet
from django.urls import reverse_lazy

# Create your views here.
def home_view(request):
    return render(request, 'home.html')

class CrearPublicacion(LoginRequiredMixin, CreateView):
    model = Publicacion
    fields = ['titulo','contenido']
    template_name = 'crear_publicacion.html'
    success_url = reverse_lazy('home') 
    
    def form_valid(self, form):
        form.instance.autor = self.request.user
        return super().form_valid(form)
    
class ListarPublicaciones(LoginRequiredMixin, ListView):
    model = Publicacion
    template_name = 'listar_publicaciones.html'
    context_object_name = 'publicaciones'
    
    def get_queryset(self):
        return Publicacion.objects.all()
    
class ListarEnDetalle(LoginRequiredMixin, DetailView):
    model = Publicacion
    template_name = 'publicacion_en_detalle.html'
    context_object_name = 'publicacion'

class EliminarPublicacion(LoginRequiredMixin, DeleteView):
    model = Publicacion
    template_name = 'confirmar_eliminar.html'
    success_url = reverse_lazy('home')
    context_object_name = 'publicacion'
    
class ActualizarPublicacion(LoginRequiredMixin, UpdateView):
    model = Publicacion
    fields = ['titulo','contenido']
    template_name = 'actualizar_publicacion.html'
    success_url = reverse_lazy('home')
    
    def form_valid(self, form):
        return super().form_valid(form)
    
class RegistroUsuario(CreateView):
    template_name = 'registro.html'
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
from django.views.generic import ListView, CreateView, DeleteView, UpdateView
from django.urls import reverse_lazy
from perfiles.models import Perfil

class PerfilList(ListView):
    model = Perfil

class PerfilCrear(CreateView):
    model = Perfil
    success_url = reverse_lazy("perfil-list")
    fields = ["nombre_usuario", "email", "contraseña"]

class PerfilBorrar(DeleteView):
    model = Perfil
    success_url = reverse_lazy("perfil-list")

class PerfilActualizar(UpdateView):
    model = Perfil
    success_url = reverse_lazy("perfil-list")
    fields = ["nombre_usuario", "email", "contraseña"]
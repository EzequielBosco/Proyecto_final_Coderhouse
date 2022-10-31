from django.shortcuts import render, get_object_or_404
from django.views import View
from django.views.generic import ListView, CreateView, DeleteView, UpdateView, DetailView
from perfiles.models import Perfil

class PerfilList(ListView):
    model = Perfil

class PerfilCrear(CreateView):
    model = Perfil
    success_url = "/accounts/profile/"
    fields = ["nombre_usuario", "email", "contraseña"]

class PerfilBorrar(DeleteView):
    model = Perfil
    success_url = "/accounts/profile/"

class PerfilActualizar(UpdateView):
    model = Perfil
    success_url = "/accounts/profile/"
    fields = ["nombre_usuario", "email", "contraseña"]
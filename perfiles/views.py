from django.shortcuts import render, get_object_or_404
from django.views import View
from django.views.generic import ListView, CreateView, DeleteView, UpdateView
from perfiles.models import Perfil
from perfiles.forms import Buscar, PerfilForm


class ListarPerfiles(View):
    template_name = "perfiles/lista_de_perfiles.html"

    def get(self, request):
        perfiles = Perfil.objects.all()
        return render(request, self.template_name, {"perfiles":perfiles})

class CargarPerfiles(View):
    template_name = "perfiles/carga_de_perfiles.html"
    form_class = PerfilForm
    initial = {"nombre_usuario":"","email":"","contraseña":""}

    def get(self, request):
        form = self.form_class(initial=self.initial)
        return render(request, self.template_name, {"form":form})

    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            form.save()
            form = self.form_class(initial=self.initial)
        return render(request, self.template_name, {"form":form})

class ActualizarPerfil(View):
    template_name = "perfiles/actualizar_perfil.html"
    success_template = "perfiles/exito.html"
    form_class = PerfilForm
    initial = {"nombre_usuario":"","email":"","contraseña":""}

    def get(self, request, pk):
        perfil = get_object_or_404(Perfil, pk=pk)
        form = self.form_class(instance=perfil)
        return render(request, self.template_name, {"form":form, "pk":pk})

    def post(self, request, pk):
        perfil = get_object_or_404(Perfil, pk=pk)
        form = self.form_class(request.POST, instance=perfil)
        if form.is_valid():
            form.save()
            form = self.form_class(initial=self.initial)
        return render(request, self.success_template)

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

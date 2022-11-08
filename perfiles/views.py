from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.admin import User
from django.views.generic import ListView, CreateView, DeleteView, UpdateView
from django.urls import reverse_lazy
from perfiles.models import Perfil

class PerfilList(ListView):
    model = Perfil
# borrar
class PerfilCrear(CreateView):
    model = Perfil
    success_url = reverse_lazy("perfil-list")
    fields = ["nombre_usuario", "email", "contraseña"]
# borrar
class PerfilBorrar(DeleteView):
    model = Perfil
    success_url = reverse_lazy("perfil-list")
# borrar
class PerfilActualizar(UpdateView):
    model = Perfil
    success_url = reverse_lazy("perfil-list")
    fields = ["nombre_usuario", "email", "contraseña"]

class BlogLogin(LoginView):
    template_name = 'perfiles/blog_login.html'
    next_page = reverse_lazy("index-blog")

class BlogLogout(LogoutView):
    template_name = 'perfiles/blog_logout.html'

class BlogSignUp(CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy("blog-login")
    template_name = "perfiles/signup.html"

class ProfileUpdate(UpdateView):
    model = User
    fields = ['username', 'first_name', 'last_name', 'email']
    success_url = reverse_lazy("blog-login")
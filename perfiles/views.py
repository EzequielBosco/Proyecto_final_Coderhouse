from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.admin import User
from django.views.generic import ListView, CreateView, DeleteView, UpdateView, DetailView
from django.urls import reverse_lazy

class BlogLogin(LoginView):
    template_name = 'perfiles/blog_login.html'
    next_page = reverse_lazy("index-blog")

class BlogLogout(LogoutView):
    template_name = 'perfiles/blog_logout.html'

class BlogSignUp(CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy("blog-login")
    template_name = "registration/signup.html"

class ProfileList(ListView):
    model = User

class ProfileBorrar(DeleteView):
    model = User
    success_url = reverse_lazy("user-list")

class ProfileUpdate(UpdateView):
    model = User
    fields = ['username', 'first_name', 'last_name', 'email']
    success_url = reverse_lazy("blog-login")

class DetailUser(DetailView):
    model = User
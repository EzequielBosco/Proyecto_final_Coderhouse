from .forms import CustomUserCreationForm
from django.contrib.auth import forms  
from django.contrib.auth.mixins import LoginRequiredMixin
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
    form_class = CustomUserCreationForm
    success_url = reverse_lazy("blog-login")
    template_name = "registration/signup.html"

class ProfileList(LoginRequiredMixin, ListView):
    model = User

class ProfileBorrar(LoginRequiredMixin, DeleteView):
    model = User
    success_url = reverse_lazy("user-list")

class ProfileUpdate(LoginRequiredMixin, UpdateView):
    model = User
    fields = ['username', 'first_name', 'last_name', 'email']
    success_url = reverse_lazy("blog-login")

class DetailUser(LoginRequiredMixin, DetailView):
    model = User
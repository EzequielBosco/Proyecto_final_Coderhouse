"""project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from blog.views import Home, About, Blogs, Contact, Post, Signup, Error404View, Error505View
from perfiles.views import PerfilList, PerfilCrear, PerfilBorrar, PerfilActualizar
from django.conf.urls import handler404, handler500

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', Home, name='pagina-principal'),
    path('about/', About, name='nosotros'),
    path('pages/', Blogs, name="blogs"),
    path('contact/', Contact, name="contacto"),
    path('pages/<int:pk>/', Post),
    path('accounts/profile/', PerfilList.as_view(), name="perfil-list"), 
    path('accounts/signup', PerfilCrear.as_view(), name="perfil-crear"),
    path('accounts/signup/crear', Signup, name="crear"),
    path('accounts/login', PerfilCrear.as_view(), name="perfil-crear"),
    path('accounts/profile/<int:pk>/borrar', PerfilBorrar.as_view(), name="perfil-borrar"),
    path('accounts/profile/<int:pk>/actualizar', PerfilActualizar.as_view(), name="perfil-actualizar"),
]

handler404 = Error404View.as_view()
handler500 = Error505View.as_error_view()
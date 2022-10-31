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
from blog.views import Home, About, Blogs, Contact, Post
from perfiles.views import PerfilList, PerfilCrear, PerfilBorrar, PerfilActualizar


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', Home),
    path('about/', About),
    path('blogs/', Blogs),
    path('contact/', Contact),
    path('pages/', Post),
    path('accounts/profile/', PerfilList.as_view()),
    path('accounts/signup', PerfilCrear.as_view()),
    path('accounts/profile/<int:pk>/borrar', PerfilBorrar.as_view()),
    path('accounts/profile/<int:pk>/actualizar', PerfilActualizar.as_view()),
]

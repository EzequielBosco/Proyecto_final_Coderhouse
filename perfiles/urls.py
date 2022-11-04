from django.urls import path
from post.views import *
from perfiles.views import PerfilList, PerfilCrear, PerfilBorrar, PerfilActualizar

urlpatterns = [
    path('accounts/profile/', PerfilList.as_view(), name="perfil-list"), 
    path('accounts/signup', PerfilCrear.as_view(), name="perfil-crear"),
    path('accounts/login', PerfilCrear.as_view(), name="perfil-entrar"),
    path('accounts/profile/<int:pk>/borrar', PerfilBorrar.as_view(), name="perfil-borrar"),
    path('accounts/profile/<int:pk>/actualizar', PerfilActualizar.as_view(), name="perfil-actualizar"),
]
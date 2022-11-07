from django.urls import path
from post.views import *
from perfiles.views import PerfilList, PerfilCrear, PerfilBorrar, PerfilActualizar,  BlogLogin, BlogLogout, BlogSignUp, ProfileUpdate

urlpatterns = [
    path('accounts/profile/', PerfilList.as_view(), name="perfil-list"), 
    path('accounts/signup', PerfilCrear.as_view(), name="perfil-crear"),
    path('accounts/profile/<int:pk>/borrar', PerfilBorrar.as_view(), name="perfil-borrar"),
    path('accounts/profile/<int:pk>/actualizar', PerfilActualizar.as_view(), name="perfil-actualizar"),
    path('login/', BlogLogin.as_view(), name="blog-login"),
    path('logout/', BlogLogout.as_view(), name="blog-logout"),
    path('signup/', BlogSignUp.as_view(), name="blog-signup"),
    path('user-profile/<int:pk>', ProfileUpdate.as_view(), name="profile-update"),
]
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
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from blog.views import Home, Blogs, Error404View, Contacto
from django.conf.urls import handler404
from blog.views import CreateComentario, ComentarioList

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', Home, name='pagina-principal'),
    path('contact/', Contacto.as_view(), name="contacto"),
    path('pages/', Blogs, name="index-blog"),
    path('accounts/', include('perfiles.urls')),
    path('pages/', include('post.urls')),
    path('comentario/', CreateComentario.as_view(), name="crear-comentario"),
    path('about/', ComentarioList.as_view(), name="nosotros"),
]

handler404 = Error404View.as_view()
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
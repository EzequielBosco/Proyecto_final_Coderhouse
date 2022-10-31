from django.contrib import admin
from blog.models import Configuracion, Blog, Blog_post

admin.site.register(Configuracion)
admin.site.register(Blog)
admin.site.register(Blog_post)
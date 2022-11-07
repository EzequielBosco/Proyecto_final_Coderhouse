from django.shortcuts import render
from django.views.generic import TemplateView
from blog.models import Configuracion

def Home(request):
    configuracion = Configuracion.objects.first()
    return render (request, "blog/index.html", {"configuracion":configuracion})

def About(request):
    return render (request, "blog/about.html")

def Contact(request):
    return render (request, "blog/contact.html")

class Error404View(TemplateView):
    template_name = "blog/error_404.html"
from django.shortcuts import render
from django.http import HttpResponse
from blog.models import Configuracion

def Home(request):
    configuracion = Configuracion.objects.first()
    return render (request, "blog/index.html", {"configuracion":configuracion})

def About(request):
    return render (request, "blog/about.html")

def Blogs(request):
    return render (request, "blog/blogs.html")

def Contact(request):
    return render (request, "blog/contact.html")

def Post(request):
    return render (request, "blog/post.html")

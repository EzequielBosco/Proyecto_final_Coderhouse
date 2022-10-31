from django.shortcuts import render
from django.http import HttpResponse

def Home(request):
    return render (request, "perfiles/index.html")

def About(request):
    return render (request, "perfiles/about.html")

def Blogs(request):
    return render (request, "perfiles/blogs.html")

def Contact(request):
    return render (request, "perfiles/contact.html")

def Post(request):
    return render (request, "perfiles/post.html")

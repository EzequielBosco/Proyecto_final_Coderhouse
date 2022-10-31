from django.shortcuts import render
from django.http import HttpResponse

def Home(request):
    return render (request, "blog/index.html")

def About(request):
    return render (request, "blog/about.html")

def Blogs(request):
    return render (request, "blog/blogs.html")

def Contact(request):
    return render (request, "blog/contact.html")

def Post(request):
    return render (request, "blog/post.html")

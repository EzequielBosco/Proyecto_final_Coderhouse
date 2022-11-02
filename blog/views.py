from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import TemplateView
from blog.models import Configuracion, Blog, Blog_post

def Home(request):
    configuracion = Configuracion.objects.first()
    return render (request, "blog/index.html", {"configuracion":configuracion})

def About(request):
    return render (request, "blog/about.html")

def Blogs(request):
    blog = Blog.objects.first()
    return render (request, "blog/blogs.html", {"blog":blog})

def Contact(request):
    return render (request, "blog/contact.html")

def Post(request):
    blog_post = Blog_post.objects.first()
    return render (request, "blog/post.html", {"blog_post":blog_post})

def Signup(request):
    return render (request, "blog/signup.html")

class Error404View(TemplateView):
    template_name = "blog/error_404.html"

class Error505View(TemplateView):
    template_name = "blog/error_500.html"

    @classmethod
    def as_error_view(cls):

        v = cls.as_view()
        def view(request):
            r = v(request)
            r.render()
            return r
        return view
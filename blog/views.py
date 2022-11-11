from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView
from django.contrib.auth.decorators import login_required
from django.views.generic import TemplateView
from blog.models import ConfigIndex, ConfigAbout, Contacto
from post.models import Post

def Home(request):
    configindex = ConfigIndex.objects.first()
    return render (request, "blog/index.html", {"configindex":configindex})

def About(request):
    configabout = ConfigAbout.objects.first()
    return render (request, "blog/about.html", {"configabout":configabout})

class Contacto(CreateView):
    model = Contacto
    fields = ['nombre', 'correo', 'numero_telefono', 'mensaje']
    success_url = reverse_lazy("pagina-principal")

@login_required
def Blogs(request):
    posts = Post.objects.order_by('-fecha').all()
    return render(request, 'blog/blogs.html', {"post":posts})

class Error404View(TemplateView):
    template_name = "blog/error_404.html"
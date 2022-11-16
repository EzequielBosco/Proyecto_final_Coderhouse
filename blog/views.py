from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView
from django.contrib.auth.decorators import login_required
from django.views.generic import TemplateView
from blog.models import Contacto, Comentario
from post.models import Post
from django.views.generic import ListView, CreateView
from blog.forms import ComentarioForm

def Home(request):
    return render (request, "blog/index.html")

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

class ComentarioList(ListView):
    model = Comentario

class CreateComentario(CreateView):
    model = Comentario
    fields = ['nombre', 'mensaje']
    success_url = reverse_lazy("nosotros")
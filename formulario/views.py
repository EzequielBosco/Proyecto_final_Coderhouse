from django.shortcuts import render

def index1(request):
    return render(request, "formulario/registro.html")
def index(request):
    return render(request, "formulario/index_blog.html")
def blog(request):
    return render(request, "formulario/blog.html")

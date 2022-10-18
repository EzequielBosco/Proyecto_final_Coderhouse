from django.shortcuts import render

def index(request):
    return render(request, "formulario/saludar.html")
def index1(request):
    return render(request, "formulario/index.html")

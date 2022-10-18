from django.shortcuts import render

def index(request):
    return render(request, "formulario/saludar.html")

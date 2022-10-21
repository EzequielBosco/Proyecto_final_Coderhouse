from django.shortcuts import render

def index0(request):
    return render(request, "app1/index0.html")
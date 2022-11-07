from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.views.generic import TemplateView
from blog.models import ConfigIndex, ConfigAbout, ConfigContact
from post.models import Post

def Home(request):
    configindex = ConfigIndex.objects.first()
    return render (request, "blog/index.html", {"configindex":configindex})

def About(request):
    configabout = ConfigAbout.objects.first()
    return render (request, "blog/about.html", {"configabout":configabout})

def Contact(request):
    configcontact = ConfigContact.objects.first()
    return render (request, "blog/contact.html", {"configcontact":configcontact})

@login_required
def Blogs(request):
    posts = Post.objects.order_by('-fecha').all()
    return render(request, 'blog/blogs.html', {"post":posts})

class Error404View(TemplateView):
    template_name = "blog/error_404.html"
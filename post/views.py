from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import ListView, CreateView, DeleteView, UpdateView, DetailView
from post.models import Post

def Blogs(request):
    post = Post.objects.first()
    return render(request, 'post/blogs.html', {"post":post})

class PostList(ListView):
    model = Post

class CreatePost(CreateView):
    model = Post
    fields = ['titulo', 'sub_titulo', 'cuerpo']
    success_url = reverse_lazy("blog-list")

class DetailPost(DetailView):
    model = Post

class UpdatePost(UpdateView):
    model = Post
    fields =['titulo', 'sub_titulo', 'cuerpo']
    success_url = reverse_lazy("blog-list")

class DeletePost(DeleteView):
    model = Post
    success_url = reverse_lazy("blog-list")


class SearchPostByname(ListView):
    def get_queryset(self):
        blog_title = self.request.GET.get('post-titulo')
        return Post.objects.filter(titulo__icontains=blog_title)
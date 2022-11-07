from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, DeleteView, UpdateView, DetailView
from post.models import Post

@login_required
def Blogs(request):
    posts = Post.objects.order_by('-fecha').all()
    return render(request, 'post/blogs.html', {"post":posts})

class PostList(LoginRequiredMixin, ListView):
    model = Post

class CreatePost(CreateView):
    model = Post
    fields = ['titulo', 'sub_titulo', 'cuerpo', 'imagen']
    success_url = reverse_lazy("blog-list")

class DetailPost(DetailView):
    model = Post

class UpdatePost(UpdateView):
    model = Post
    fields =['titulo', 'sub_titulo', 'cuerpo', 'imagen']
    success_url = reverse_lazy("blog-list")

class DeletePost(DeleteView):
    model = Post
    success_url = reverse_lazy("blog-list")


class SearchPostByname(ListView):
    def get_queryset(self):
        post_title = self.request.GET.get('post-titulo')
        return Post.objects.filter(titulo__icontains=post_title)
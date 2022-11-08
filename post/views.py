from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, DeleteView, UpdateView, DetailView
from post.models import Post

class PostList(LoginRequiredMixin, ListView):
    model = Post

class CreatePost(CreateView):
    model = Post
    fields = ['autor', 'titulo', 'sub_titulo', 'cuerpo', 'imagen']
    success_url = reverse_lazy("blog-list")

class DetailPost(DetailView):
    model = Post

class UpdatePost(UpdateView):
    model = Post
    fields =['autor', 'titulo', 'sub_titulo', 'cuerpo', 'imagen']
    success_url = reverse_lazy("blog-list")

class DeletePost(DeleteView):
    model = Post
    success_url = reverse_lazy("blog-list")


class SearchPostByname(ListView):
    def get_queryset(self):
        post_title = self.request.GET.get('post-titulo')
        return Post.objects.filter(titulo__icontains=post_title)
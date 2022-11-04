from django.urls import path
from post.views import *
from post.views import PostList, CreatePost, DetailPost, UpdatePost, DeletePost, SearchPostByname, BlogLogin, BlogLogout, BlogSignUp, ProfileUpdate

urlpatterns = [
    path('', Blogs, name="index-blog"),
    path('list/', PostList.as_view(), name="blog-list"),
    path('create/', CreatePost.as_view(), name="blog-crear"),
    path('detail/<int:pk>/', DetailPost.as_view(), name="blog-detail"),
    path('update/<int:pk>/', UpdatePost.as_view(), name="blog-actualizar"),
    path('delete/<int:pk>', DeletePost.as_view(), name="blog-borrar"),
    path('search-by-name/', SearchPostByname.as_view(), name="search-by-name-post"),
    path('login/', BlogLogin.as_view(), name="blog-login"),
    path('logout/', BlogLogout.as_view(), name="blog-logout"),
    path('signup/', BlogSignUp.as_view(), name="blog-signup"),
    path('user-profile/<int:pk>', ProfileUpdate.as_view(), name="profile-update"),
]
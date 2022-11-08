from django.urls import path
from post.views import *
from perfiles.views import BlogLogin, BlogLogout, BlogSignUp, ProfileUpdate, ProfileBorrar, ProfileList, DetailUser

urlpatterns = [
    path('profile/', ProfileList.as_view(), name="user-list"), 
    path('user-profile/<int:pk>/borrar/', ProfileBorrar.as_view(), name="profile-borrar"),
    path('user-profile/<int:pk>', ProfileUpdate.as_view(), name="profile-update"),
    path('detail/<int:pk>/', DetailUser.as_view(), name="profile-detail"),
    path('login/', BlogLogin.as_view(), name="blog-login"),
    path('logout/', BlogLogout.as_view(), name="blog-logout"),
    path('signup/', BlogSignUp.as_view(), name="blog-signup"),
]
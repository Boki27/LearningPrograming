from django.urls import path
from . import views

urlpatterns = [
    path('', views.posts_list, name="posts"),
    path('new-post/', views.post_new, name="new-post"),
    path('<slug:slug>', views.post_page, name="page"),
]
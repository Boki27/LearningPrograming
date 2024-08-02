from django.shortcuts import render, get_object_or_404, redirect
from .models import Post
from django.contrib.auth.decorators import login_required
from . import forms

# Create your views here.
def posts_list(request):
  posts = Post.objects.all().order_by('-date')
  return render(request, 'posts/posts_list.html', {'posts': posts})


def post_page(request, slug):
    posts = Post.objects.filter(slug=slug)
    if posts.exists():
        post = posts.first()  # or handle multiple posts as needed
    else:
        post = get_object_or_404(Post, slug=slug)
    return render(request, 'posts/post_page.html', {'post': post})

@login_required(login_url="/users/login/")
def post_new(request):
    if request.method == 'POST':
        form = forms.CreatePost(request.POST, request.FILES)
        if form.is_valid():
            # save with user
            newpost = form.save(commit=False)
            newpost.author = request.user
            newpost.save()
            return redirect('posts')
    else:
        form = forms.CreatePost()
    return render(request, 'posts/post_new.html', { 'form': form })
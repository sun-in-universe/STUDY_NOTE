from django.shortcuts import render, redirect, get_object_or_404, HttpResponse
from django.core.paginator import Paginator
from django.views import View
from django.views.generic import (
    CreateView, ListView, DetailView, UpdateView, 
    DeleteView, RedirectView,
)
from django.urls import reverse
from .models import Post, Comment
from .forms import PostForm, CommentForm

# Create your views here.
def index(request):
    return render(request, 'post/post_list.html')


def post_list(request):
    posts = Post.objects.all()
    context = {'posts': posts}
    return render(request, 'post/post_list.html', context)


def post_detail(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    context = {'post': post}
    return render(request, 'post/post_detail.html', context)


def post_create(request):
    if request.method == 'POST':
        post_form = PostForm(request.POST)
        if post_form.is_valid():
            new_post = post_form.save()
            return redirect('posts:post_list')
    else:
        post_form = PostForm()
    return render(request, 'post/post_form.html', {'form': post_form})


def post_edit(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    if request.method == 'POST':
        post_form = PostForm(request.POST, instance=post)
        if post_form.is_valid():
            post_form.save()
            return redirect('posts:post_detail', post_id=post_id)
    else:
        post_form = PostForm(instance=post)
    return render(request, 'post/post_form.html', {'form': post_form})


def post_delete(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    if request.method == 'POST':
        post.delete()
        return redirect('posts:post_list')
    else:
        return render(request, 'post/post_confirm_delete.html', {'post': post})
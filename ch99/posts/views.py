from django.shortcuts import render, redirect, get_object_or_404, HttpResponse
from django.core.paginator import Paginator
from django.views import View
from django.urls import reverse
from .models import Post, Comment
from .forms import PostForm, CommentForm

# 목록
def index(request):
    return render(request, 'post/post_list.html')

# 첫페이지
def post_list(request):
    posts = Post.objects.all()
    context = {'posts': posts}
    return render(request, 'post/post_list.html', context)

# 상세페이지
def post_detail(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    context = {'post': post}
    return render(request, 'post/post_detail.html', context)

#글 쓰기
def post_create(request):
    if request.method == 'POST':
        post_form = PostForm(request.POST)
        if post_form.is_valid():
            new_post = post_form.save()
            return redirect('posts:post_list')
    else:
        post_form = PostForm()
    return render(request, 'post/post_form.html', {'form': post_form})

# 수정하기 
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

# 삭제하기
def post_delete(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    if request.method == 'POST':
        post.delete()
        return redirect('posts:post_list')
    else:
        return render(request, 'post/post_confirm_delete.html', {'post': post})

# 댓글달기 
def comment(request, post_id):
    if request.method == 'POST':
        post = Post.objects.get(id=post_id)
        comment_form = CommentForm(request.POST)  # 댓글을 입력하는 양식의 이름을 사용
        if comment_form.is_valid():
            content = comment_form.cleaned_data['content']
            comment = Comment(post=post, content=content)
            comment.save()
            return redirect('post_detail', post_id=post_id)  # 댓글을 작성한 후 게시물 페이지로 리디렉션
    else:
        # GET 요청 처리 (댓글 양식을 표시하는 로직)
        post = Post.objects.get(id=post_id)
        comment_form = CommentForm()  # 댓글을 입력하는 양식의 이름을 사용

    return render(request, 'post/comment_form.html', {'post': post, 'comment_form': comment_form})

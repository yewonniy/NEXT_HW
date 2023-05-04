from django.shortcuts import render, redirect
from .models import Post, Comment
from django.contrib.auth.models import User
from django.contrib import auth
from django.contrib.auth.decorators import login_required

# Create your views here.

def home(request):
    posts = Post.objects.all() #all -> queryset method

    return render(request, 'app/home.html', {'posts':posts})

@login_required(login_url="/accounts/registration/login/")
def new(request):
    if request.method == "POST":
        new_post = Post.objects.create(
            title = request.POST['title'],
            content = request.POST['content'],
            author = request.user
        )
        return redirect('app:detail', new_post.pk)
    
    return render(request, 'app/new.html')

@login_required(login_url="/accounts/registration/login/")
def detail(request,	post_pk):
    post = Post.objects.get(pk=post_pk)

    if request.method == "POST":
        Comment.objects.create(
            post = post,
            content = request.POST['content'],
            author = request.user
        )
        return redirect('app:detail', post_pk)

    return render(request, 'app/detail.html', {'post':post}) #html에서 사용해야하는 이름은 주황색 post

def update(request,	post_pk):
    post = Post.objects.get(pk=post_pk)

    if request.method == 'POST':
        Post.objects.filter(pk=post_pk).update(
            title = request.POST['title'], #html form태그에 있는 값
            content = request.POST['content']
        )
        return redirect('app:detail', post_pk)
    #filter -> 쿼리셋을 가져옴, get -> 객체 하나를 가져옴
    return render(request, 'app/update.html', {'post':post})

def delete(request,	post_pk):
    post = Post.objects.get(pk=post_pk)
    post.delete()

    return redirect('app:home')

def delete_comment(request, post_pk, comment_pk):
   comment = Comment.objects.get(pk=comment_pk)
   comment.delete()
   return redirect('app:detail', post_pk)
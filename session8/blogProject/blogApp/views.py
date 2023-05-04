from django.shortcuts import render, redirect
from django.contrib import auth
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .models import Article, Category, Comment, Recomment
from datetime import datetime

# Create your views here.
def new(request):
    if request.method == 'POST':
        print(request.POST)
        cate_gory = request.POST['category'] #cate_gory는 카테고리명 str
        cate = Category.objects.get(name=cate_gory) #cate는 객체

        new_article = Article.objects.create(
            title = request.POST['title'],
            content = request.POST['content'],
            time = datetime.now(),
            category = cate, #객체를 넘겨준다
        )

        return redirect('detail',new_article.pk)
    
    return render(request, 'new.html')

def list(request):
    articles = Article.objects.all() #모든 글 조회!
    hobby_cate = Category.objects.get(name="hobby") #hobby라는 Category 자체를 가져온 거
    daily_cate = Category.objects.get(name="daily")
    programming_cate = Category.objects.get(name="programming")

    hobbies = Article.objects.filter(category = hobby_cate)
    dailys = Article.objects.filter(category = daily_cate)
    programmings = Article.objects.filter(category = programming_cate)

    cnt_all = articles.count()
    cnt_hobby = hobbies.count()
    cnt_daily = dailys.count()
    cnt_programming = programmings.count()
    return render(request, 'list.html', {'articles':articles, 'cnt_all':cnt_all, 'cnt_hobby':cnt_hobby, 'cnt_daily': cnt_daily, 'cnt_programming':cnt_programming}) 
    # render함수의 인자 -> request, 렌더링 시킬거, 딕셔너리(위의 변수 articles에 담았던 값을 articles라는 이름으로 template에 보내준다?.?)

def hobby(request):
    hobby_cate = Category.objects.get(name="hobby")
    hobby_ = Article.objects.filter(category = hobby_cate)
    return render(request, 'hobby.html', {'hobby_':hobby_})

def daily(request):
    daily_cate = Category.objects.get(name="daily")
    daily_ = Article.objects.filter(category = daily_cate)
    return render(request, 'daily.html', {'daily_':daily_})

def programming(request):
    prog_cate = Category.objects.get(name="programming")
    program_ = Article.objects.filter(category = prog_cate)
    return render(request, 'programming.html', {'program_':program_})

def edit(request, article_id):
   details = Article.objects.get(id=article_id)

   if request.method == 'POST':
       title = request.POST['title']
       content = request.POST['content']
       Article.objects.filter(id=article_id).update(
           title=title,
           content=content
       )
       return redirect('detail', article_id)
   
   return render(request, 'edit.html', {'details':details})


def delete(request, article_id):
   details = Article.objects.get(id=article_id)
   details.delete()
   return redirect('list')

#---------------------------------------


def delete_comment(request, article_id , comment_pk):
    comment = Comment.objects.get(id = comment_pk)
    comment.delete()
    return redirect('detail', article_id)


def re_comment(request, article_id, comment_id):
    details = Article.objects.get(id = article_id)
    comment = Comment.objects.get(id = comment_id)

    if request.method == "POST":
        re_content = request.POST['re_comment']
        Recomment.objects.create(
            comment = comment,
            re_content = re_content
        )
        return redirect('detail', article_id)
    
    return render(request, 'detail.html', {'details':details})

#-----------------------------------------------

def signup(request):
   if request.method == 'POST':
      username = request.POST['username']
      password = request.POST['password']
      exist_user = User.objects.filter(username=username)
      if exist_user:
           error = "이미 존재하는 유저입니다."
           return render(request, 'registration/signup.html', {"error":error})
      
      new_user = User.objects.create_user(username=username, password=password)
      auth.login(request, new_user)
   
      return redirect('home')
       
   return render(request, 'registration/signup.html')

def login(request):
   if request.method == 'POST':
      username = request.POST['username']
      password = request.POST['password']
      user = auth.authenticate(username=username, password=password)
      if user is not None:
           auth.login(request, user, backend ="django.contrib.auth.backends.ModelBackend")
           return redirect(request.GET.get('next', '/'))
      error = "아이디 또는 비밀번호가 틀립니다"
      return render(request, 'registration/login.html', {"error":error})
        
   return render(request, 'registration/login.html')

def logout(request):
   auth.logout(request)
   return redirect('home')

@login_required(login_url="/registration/login/")
def new(request):
    if request.method == 'POST':
        print(request.POST)
        cate_gory = request.POST['category'] #cate_gory는 카테고리명 str
        cate = Category.objects.get(name=cate_gory) #cate는 객체

        new_article = Article.objects.create(
            title = request.POST['title'],
            content = request.POST['content'],
            time = datetime.now(),
            category = cate, #객체를 넘겨준다
        )

        return redirect('detail',new_article.pk)
    
    return render(request, 'new.html')

@login_required(login_url="/registration/login/")
def detail(request, article_id):
    details = Article.objects.get(id = article_id)

    if request.method == 'POST':
        content = request.POST['content']
        Comment.objects.create(
            post = details,
            content = content
        )
        return redirect('detail', article_id)
    
    return render(request, 'detail.html', {'details':details})
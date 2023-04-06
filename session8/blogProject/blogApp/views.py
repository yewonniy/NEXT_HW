from django.shortcuts import render, redirect
from .models import Article, Category
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

def detail(request, article_id):
    details = Article.objects.get(id = article_id)
    return render(request, 'detail.html', {'details':details})

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
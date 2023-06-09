"""blogProject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from blogApp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.list, name="home"),
    path('new', views.new, name='new'), #name = new : url의 별명을 new라고 하겠다는 뜻
    path('list/', views.list, name='list'),
    path('detail/<int:article_id>/', views.detail, name='detail'), #article_id는 그냥 내가 만든 변수명! . 은 접근연산자
    path('hobby/', views.hobby, name='hobby'),
    path('daily/', views.daily, name='daily'),
    path('programming/', views.programming, name='programming'),
    path('edit/<int:article_id>', views.edit, name='edit'),
    path('delete/<int:article_id>', views.delete, name='delete'),
    path('delete-comment/<int:article_id>/<int:comment_pk>', views.delete_comment, name='delete-comment'),
    path('new_recomment/<int:article_id>/<int:comment_id>',views.re_comment, name='new_recomment'),
    path("registration/signup/", views.signup, name="signup"),
    path("registration/login/", views.login, name="login"),
    path("registration/logout/", views.logout, name="logout"),
    path('accounts/', include('allauth.urls')),
]

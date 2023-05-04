#blog 밑에 있는 이 urls.py는 내가 직접 만든 거
from django.urls import path
from app import views 

app_name = 'app'
# 중복을 피하기 위한 url 네임스페이스

urlpatterns = [
    #앞에 /app/ 가 생략되어 있는 것
    path('', views.home, name = 'home'),
    path('new/', views.new,	name="new"), #저 물리적 이름 'home'은 (1) .html의 a태그 href나 (2) views.py에서 redirect에 쓰임
    path('detail/<int:post_pk>/', views.detail,	name="detail"),
    path('update/<int:post_pk>/', views.update,	name="update"),
    path('delete/<int:post_pk>/', views.delete,	name="delete"),
    path('delete-comment/<int:post_pk>/<int:comment_pk>', views.delete_comment, name='delete_comment'),
]
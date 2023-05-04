from django.urls import path
from accounts	import views

app_name = 'accounts' 
urlpatterns = [
    #/accounts/
    path('', views.home, name = 'home'),
    path("registration/signup/", views.signup, name="signup"),
    path('registration/login/', views.login, name= "login"),
    path('registration/logout/', views.logout, name="logout"),
]
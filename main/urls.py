from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('contacts/', views.contacts, name='contacts'),
    path('services/', views.services, name='services'),
    path('profile/', views.profile, name='profile'),
    path('articles/', views.articles, name='articles'),
    path('articles/<int:article_id>/', views.article_detail, name='article_detail'),
    path('article/create/', views.article_create, name='article_create'),
    path('video/', views.videopost, name='video'),
    path('register/', views.register, name='register'),
    path('login/', views.user_login, name='login'),
    path('logout/', views.user_logout, name='logout'),
]

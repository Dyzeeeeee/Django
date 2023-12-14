# posts/urls.py
from django.urls import path
from .views import post_list, news_feed

urlpatterns = [
    path('posts/', post_list, name='post_list'),
    path('news-feed/', news_feed, name='news_feed'),
]

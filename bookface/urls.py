# bookface/urls.py
from django.urls import path
from .views import (
    home,
    create_post,
    post_detail,
    register_view,
    login_view,
    logout_view,
    view_profile,
    chat_room,
    send_message
)

urlpatterns = [
    path("", home, name="home"),
    path("post/create", create_post, name="create_post"),
    path("post/<int:post_id>/", post_detail, name="post_detail"),
    path("register/", register_view, name="register"),
    path("login/", login_view, name="login"),
    path("logout/", logout_view, name="logout"),
    path('profile/<str:username>/', view_profile, name='view_profile'),
    path('chat/<str:username>', chat_room, name='chat_room'),
    # path('chat/<str:username>/send_message/', send_message, name='send_message'),
]

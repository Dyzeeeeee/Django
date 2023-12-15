# bookface/views.py
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from .models import Post, UserProfile, Message
from .forms import PostForm, UserProfileForm, MessageForm
from django.contrib.auth.models import User
from django.urls import reverse_lazy
from django.db import models
from django.http import JsonResponse
from django.db.models import Q
from django.views.decorators.http import require_POST


def register_view(request):
    if request.user.is_authenticated:
        return redirect("home")  # Redirect to home if user is already logged in

    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect("home")  # Change 'home' to the name of your home view
    else:
        form = UserCreationForm()
    return render(request, "register.html", {"form": form})


def login_view(request):
    if request.user.is_authenticated:
        return redirect("home")  # Redirect to home if user is already logged in

    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect("home")  # Change 'home' to the name of your home view
    else:
        form = AuthenticationForm()
    return render(request, "login.html", {"form": form})


def logout_view(request):
    logout(request)
    return redirect("login")  # Change 'login' to the name of your login view


@login_required(login_url=reverse_lazy("login"))
def home(request):
    posts = Post.objects.all().order_by("-created_at")
    user = request.user

    # Get a list of users with whom the current user has chatted
    chat_list = (
        Message.objects.filter(Q(sender=user) | Q(receiver=user))
        .order_by("-timestamp")
        .values("sender", "receiver")
        .distinct()
    )

    return render(request, "home.html", {"posts": posts, "chat_list": chat_list})


@login_required(login_url=reverse_lazy("login"))
def create_post(request):
    if request.method == "POST":
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            return redirect("home")
    else:
        form = PostForm()
    return render(request, "create_post.html", {"form": form})


def post_detail(request, post_id):
    post = Post.objects.get(pk=post_id)
    return render(request, "post_detail.html", {"post": post})


def view_profile(request, username):
    user = get_object_or_404(User, username=username)
    profile = UserProfile.objects.get_or_create(user=user)[0]

    if request.method == "POST":
        form = UserProfileForm(request.POST, request.FILES, instance=profile)
        if form.is_valid():
            form.save()
    else:
        form = UserProfileForm(instance=profile)

    return render(request, "profile.html", {"user": user, "form": form})

@login_required(login_url=reverse_lazy("login"))
def chat_room(request, username):
    other_user = get_object_or_404(User, username=username)
    messages = Message.objects.filter(
        (
            models.Q(sender=request.user, receiver=other_user)
            | models.Q(sender=other_user, receiver=request.user)
        )
    ).order_by("timestamp")

    # Get a list of users with whom the current user has chatted
    chat_list = get_chat_list(request.user)

    if request.method == "POST":
        form = MessageForm(request.POST)
        if form.is_valid():
            message = form.save(commit=False)
            message.sender = request.user
            message.receiver = other_user
            message.save()
            return redirect("chat_room", username=username)
    else:
        form = MessageForm()

    context = {
        "other_user": other_user,
        "messages": messages,
        "form": form,
        "chat_list": chat_list,
    }
    return render(request, "chat_room.html", context)

@require_POST
@login_required(login_url=reverse_lazy("login"))
def send_message(request, username):
    other_user = get_object_or_404(User, username=username)
    content = request.POST.get("content", "")

    if content:
        message = Message.objects.create(
            sender=request.user, receiver=other_user, content=content
        )
        return JsonResponse({"success": True, "message_id": message.id})
    else:
        return JsonResponse({"success": False, "error": "Content cannot be empty"})

def get_chat_list(user):
    # Get a list of users with whom the current user has chatted
    chat_list = (
        Message.objects.filter(Q(sender=user) | Q(receiver=user))
        .order_by("-timestamp")
        .values("sender", "receiver")
        .distinct()
    )

    return chat_list
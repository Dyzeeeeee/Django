# posts/views.py
from django.shortcuts import render
from .models import Post
from accounts.models import CustomUser  # Import your CustomUser model


def post_list(request):
    posts = Post.objects.all()
    return render(request, "posts/post_list.html", {"posts": posts})


def news_feed(request):
    # Check if the user is authenticated
    if request.user.is_authenticated:
        # Fetch posts from users that the current user follows
        following_users = request.user.following.all()
        custom_user = CustomUser.objects.get(pk=request.user.pk)

        # Print the posts associated with each following user
        # Fetch posts from users that the current user follows
        posts = Post.objects.filter(user__in=following_users).order_by("-created_at")

        return render(
            request,
            "posts/news_feed.html",
            {"posts": posts, "custom_user": custom_user},
        )
    else:
        # Handle the case when the user is not authenticated (AnonymousUser)
        # For example, you can redirect them to the login page
        return render(request, "posts/news_feed.html", {"posts": []})

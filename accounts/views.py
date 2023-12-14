from django.shortcuts import render, redirect
from .forms import RegistrationForm, LoginForm
from .models import CustomUser


def register(request):
    if request.method == "POST":
        form = RegistrationForm(request.POST)
        if form.is_valid():
            # Create a new user in the database
            user = CustomUser(
                firstname=form.cleaned_data["firstname"],
                lastname=form.cleaned_data["lastname"],
                email=form.cleaned_data["email"],
                password=form.cleaned_data["password"],
            )
            user.save()
            return redirect(
                "login"
            )  # Redirect to the login page after successful registration
    else:
        form = RegistrationForm()

    return render(request, "accounts/register.html", {"form": form})


def user_login(request):
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data["email"]
            password = form.cleaned_data["password"]

            # Check if the user exists in the database
            try:
                user = CustomUser.objects.get(email=email, password=password)
                # Log the user in (you may want to use Django's authentication system here)
                return redirect(
                    "/posts/posts"
                )  # Redirect to your home page after successful login
            except CustomUser.DoesNotExist:
                # Handle invalid login credentials
                pass
    else:
        form = LoginForm()

    return render(request, "accounts/login.html", {"form": form})

from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from .forms import UserRegistrationForm, UserLoginForm


def user_register(request):
    if request.method == "POST":
        form = UserRegistrationForm(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect("login")
    else:
        form = UserRegistrationForm()
    return render(
        request,
        "account/register.html",
        {"form": form}
    )


def user_login(request):
    if request.method == "POST":
        form = UserLoginForm(data=request.POST)
        if form.is_valid():
            username = form.cleaned_data["username"]
            password = form.cleaned_data["password"]
            user = authenticate(request, username=username, password=password)
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return redirect("dashboard")
            else:
                return render(
                    request,
                    "account/login.html",
                    {"form": form}
                )
    else:
        form = UserLoginForm()
    return render(
        request,
        "account/login.html",
        {"form": form}
    )

@login_required
def dashboard(request):
    return render(request, "account/dashboard.html") 

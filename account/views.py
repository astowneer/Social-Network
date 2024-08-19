from django.urls import reverse
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from .forms import UserRegistrationForm, UserLoginForm, UserEditForm, ProfileEditForm
from .models import Profile


def user_register(request):
    if request.method == "POST":
        form = UserRegistrationForm(data=request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "User successfully register!")
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
                    messages.add_message(request, messages.SUCCESS, "Hello world.")
                    login(request, user)
                    # messages.success(request, "Profile details updated.")
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


@login_required
def user_edit(request):
    if request.method == "POST":
        user_form = UserEditForm(request.POST or None, instance=request.user)
        profile_form = ProfileEditForm(request.POST or None, request.FILES, instance=request.user.profile)
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            return redirect(reverse("edit"))
    else:
        user_form = UserEditForm(instance=request.user)
        profile_form = ProfileEditForm(instance=request.user.profile)
    return render(
        request,
        "account/edit.html",
        {"user_form": user_form, "profile_form": profile_form}
    )
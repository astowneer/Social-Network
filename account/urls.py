from django.contrib.auth.views import PasswordResetView, PasswordResetDoneView, PasswordResetCompleteView, PasswordResetConfirmView, PasswordChangeView, PasswordChangeDoneView, LoginView, LogoutView
from django.urls import path
from . import views


urlpatterns = [
    path("dashboard/", views.dashboard, name="dashboard"),
    path("register/", views.user_register, name="register"),
    # path("login/", views.user_login, name="login"),
    path("login/", LoginView.as_view(template_name="account/login.html"), name="login"),
    path("logout/", LogoutView.as_view(), name="logout"),
    path("password-change/", PasswordChangeView.as_view(template_name="account/password_change.html"), name="password_change"),
    path("password-change/done/", PasswordChangeDoneView.as_view(template_name="account/password_change_done.html"), name="password_change_done"),
    
    path(
        "password-reset/", 
        PasswordResetView.as_view(template_name="account/password_reset_form.html"),
        name="password_reset"
    ),
    path(
        "password-reset/done/", 
        PasswordResetDoneView.as_view(template_name="account/password_reset_done.html"), 
        name="password_reset_done"
    ),
    path(
        "password-reset/<uidb64>/<token>/", 
        PasswordResetConfirmView.as_view(template_name="account/password_reset_confirm.html"),
        name="password_reset_confirm"
    ),
    path(
        "password-reset/complete/", 
        PasswordResetCompleteView.as_view(template_name="account/password_reset_complete.html"), 
        name="password_reset_complete"
    ),
]
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.contrib import messages
from .models import Profile


class UserLoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)

    # def form_valid(self, form):
    #     response = super().form_valid(form)
    #     messages.success(self.request, f'Nice')
    #     return response


class UserRegistrationForm(UserCreationForm):
    usable_password = None
    password1 = forms.CharField(label="Password", widget=forms.PasswordInput)
    password2 = forms.CharField(label="Password confirmation", widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ["username", "first_name", "email"]

    def clean_password2(self):
        # Check weather password entries matches
        cd = self.cleaned_data
        password1 = cd["password1"]
        password2 = cd["password2"]
        if password1 != password2:
            raise ValidationError("Passwords didn't matches")
        return password2
    
    def clean_email(self):
        email = self.cleaned_data["email"]
        if User.objects.filter(email=email).exists():
            raise ValidationError("User with email already exists")
        return email

class ProfileEditForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ["date_of_birth", "photo"]


class UserEditForm(forms.ModelForm):
    username = forms.CharField(max_length=155)
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ["username", "email"]

    def clean_email(self):
        email = self.cleaned_data["email"]
        if (User.objects.filter(email=email)
            .exclude(pk=self.instance.pk)
            .exists()):
            raise ValidationError("The user with this email already exists")
        return email
            

    
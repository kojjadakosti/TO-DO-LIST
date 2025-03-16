from django import forms
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm

from users.models import User


class UserRegistrationForm(UserCreationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control py-4'}))
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={
        'class': 'form-control py-4'}))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={
        'class': 'form-control py-4'}))
    email = forms.CharField(widget=forms.EmailInput(attrs={
        'class': 'form-control py-4'}))

    class Meta:
        model = User
        fields = ('username', 'password1', 'password2', 'email')


class UserLoginForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control py-4'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={
        'class': 'form-control py-4'}))

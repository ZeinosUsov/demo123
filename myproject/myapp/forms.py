from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class CustomUserCreationForm(UserCreationForm):
    fio = forms.CharField(max_length=100, label='ФИО')
    phone = forms.CharField(max_length=20, label='Телефон')

    class Meta:
        model = User
        fields = ['username', 'fio', 'phone', 'password1', 'password2']
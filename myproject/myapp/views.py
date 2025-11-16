from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib import messages
from .forms import CustomUserCreationForm
from .models import UserProfile

def my_page(request):
    return render(request, 'home.html')

def profile(request):
    return render(request, 'profile.html')

def register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            UserProfile.objects.create(
                user=user,
                fio=form.cleaned_data['fio'],
                phone=form.cleaned_data['phone']
            )
            messages.success(request, 'Аккаунт успешно создан!')
            return redirect('login')
    else:
        form = CustomUserCreationForm()
    return render(request, 'register.html', {'form': form})
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import LoginForm, CreateUserForm, UserProfileEditForm
from .models import User


def user_registration_view(request):
    form = CreateUserForm()
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')

    return render(request, 'users/registration.html', {'form': form})


def user_login_view(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            user = authenticate(request, username=form.cleaned_data['username'],
                                password=form.cleaned_data['password'])
            if user is not None:
                login(request, user)
                return redirect('profile')
            else:
                return HttpResponse('Incorrect username or password')
    else:
        form = LoginForm()
    context = {
        'form': form
    }
    return render(request, 'users/login.html', context)


@login_required(login_url='users/login.html')
def user_profile_view(request):
    user_profile = User.objects.get(id=request.user.id)
    context = {'profile': user_profile}
    return render(request, 'users/profile.html', context)


@login_required(login_url='users/login.html')
def user_profile_edit(request):
    form = UserProfileEditForm(request.POST, instance=request.user)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('profile')

    return render(request, 'users/profile_editor.html', {'form': form})


def user_logout(request):
    logout(request)

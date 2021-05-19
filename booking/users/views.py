from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import LoginForm, CreateUserForm


# Login
def user_registration_view(request):
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')

        context = {
            'form': form,
        }
    return render(request, 'users/registration.html', context)


def user_login_view(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            user = authenticate(request, username=form.cleaned_data['username'],
                                password=form.cleaned_data['password'])
            if user is not None:
                login(request, user)
            else:
                return HttpResponse('Incorrect username or password')

        context = {
            'form': form,
        }
        return render(request, 'users/login.html', context)


# Logout
def user_logout(request):
    logout(request)

# Create your views here.

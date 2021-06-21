from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.hashers import check_password
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

    context = {
        'profile': user_profile,
    }
    return render(request, 'users/profile.html', context)


@login_required(login_url='users/login.html')
def user_profile_edit(request):
    form = UserProfileEditForm(instance=request.user)
    user_profile = User.objects.get(id=request.user.id)
    if request.method == 'POST':
        form = UserProfileEditForm(request.POST, request.FILES, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('profile')

    return render(request, 'users/profile_editor.html', {
        'form': form,
        'profile': user_profile
    })

@login_required(login_url='users/login.html')
def user_logout(request):
    logout(request)
    return redirect('login')


def change_password(request):
    u = User.objects.get(username=request.user)
    if request.method == 'POST':
        form = ChangePasswordForm(request.POST)
        if form.is_valid():
            old_password = request.POST.get("old_password")
            new_pass = request.POST.get("new_password")
            new_pass_rep = request.POST.get("new_password_repeat")
            if check_password(old_password,u.password):
                return HttpResponse('ok')
            else:
                return HttpResponse('bad')
    else:
            form = ChangePasswordForm()

    return render(request, 'login/change_password.html',
              {'form': form, 'user': u})



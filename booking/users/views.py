from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.hashers import check_password
from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import LoginForm, CreateUserForm, UserProfileEditForm
from .models import User
import json
import csv


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


@login_required(login_url='users/login.html')
def account_del(request):
    if request.method == 'POST':
        u = User.objects.get(id=request.user.id)
        u.delete()
        return render(request, 'users/you_have_deleted_yourself.html')
    return render(request, 'users/account_del.html')


# @login_required(login_url='users/login.html')
# def json_get_file(request):
#     if request.method == 'POST':
#         data = User.objects.values(id=request.user.id)
#         json_user = json.dumps(data)
#         with open ('user_data', 'w') as file:
#             json.dump(json_user, file, indent=2)


@login_required(login_url='users/login.html')
def user_data_file(request):
    if request.method == 'GET':
        data = User.objects.filter(id=request.user.id).values()[0]
        json_user = json.dumps(data, indent=2, default=str)
        u = User.objects.get(id=request.user.id)
        username = u.username
        response = HttpResponse(
            json_user,
            content_type='text/csv',
            headers={'Content-Disposition': f'attachment; filename="{username}.csv"'},
        )
        return response






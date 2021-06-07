from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import LoginForm, CreateUserForm
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
                return redirect('main_page')
            else:
                return HttpResponse('Incorrect username or password')
    else:
        form = LoginForm()
    context = {
        'form': form
    }
    return render(request, 'users/login.html', context)

def user_profile_view(request):
    user_profile = User.objects.get(id=request.user.id)
    context = {'profile': user_profile}
    return render(request, 'profile', context)

# def user_forgot_pass_view(PasswordResetView):
#     if request.method == 'POST':
#         form = ForgotPassForm(request.POST)
#         if form.is_valid():
#             pass


# Logout
def user_logout(request):
    logout(request)

# Create your views here.

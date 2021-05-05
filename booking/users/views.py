from django.contrib.auth import authenticate, login, logout


# Login
def user_login(request):
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(request, username=username, password=password)
    if user is not None:
        login(request, user)
    else:
        print("Неверный логин либо пароль")


# Logout
def user_logout(request):
    logout(request)

# Create your views here.

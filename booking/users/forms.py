from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import User, EmailSender
from django.utils.translation import gettext_lazy


class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'first_name', 'last_name', 'phone', 'sex', 'password1', 'password2']


class UserProfileCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = '__all__'


class UserProfileEditForm(UserChangeForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'photo', 'first_name', 'last_name', 'phone', 'sex', 'country', 'town',
                  'card', 'valid_thru', 'language', 'currency']


class LoginForm(forms.Form):
    username = forms.CharField(label=gettext_lazy('Username'), max_length=30)
    password = forms.CharField(label=gettext_lazy('Password'), widget=forms.PasswordInput)


class SendEmail(forms.Form):
    model = EmailSender
    fields = ['adresses', 'text']

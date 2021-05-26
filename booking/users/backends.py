
from django.contrib.auth.backends import BaseBackend
from django.contrib.auth.models import User
from django.db.models import Q


class UsernamePhoneEmailBackend(BaseBackend):
    def check_user(self, username, password):
        try:
            user = User.objects.get(Q(username=username) | Q(email=username) | Q(phone=username))
        except User.DoesNotExist:
            return None
        else:
            if user.check_password(password):
                return user

    def get_user(self, user_id):
        try:
            user = User.objects.get(pk=user_id)
        except User.DoesNotExist:
            return None
        return user

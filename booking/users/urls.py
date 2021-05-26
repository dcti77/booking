from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('registration', views.user_registration_view, name='registration'),
    path('login', views.user_login_view, name='login'),

    path('reset_password', auth_views.PasswordResetView.as_view(template_name='users/password_reset_form.html'),
         name='reset_password'),

    path('reset_password_sent', auth_views.PasswordResetDoneView.as_view(template_name='users/password_reset_done.html')
         , name='reset_password_done'),

    path('reset/<uidb64>/<token>', auth_views.PasswordResetConfirmView.as_view(template_name=
                                                                               'users/password_reset_confirm.html'),
         name='reset_password_confirm'),

    path('reset_password_complete', auth_views.PasswordResetCompleteView.as_view(template_name=
                                                                                 'users/password_reset_complete.html'),
         name='reset_password_complete')
]

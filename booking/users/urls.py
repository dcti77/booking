from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('registration', views.user_registration_view, name='registration'),
    path('login', views.user_login_view, name='login'),
    path('profile', views.user_profile_view, name='profile'),
    path('edit_profile', views.user_profile_edit, name='edit_profile'),

    path('reset_password', auth_views.PasswordResetView.as_view(template_name='users/password_reset_form.html'),
         name='reset_password'),

    path('reset_password_sent', auth_views.PasswordResetDoneView.as_view(template_name='users/password_reset_done.html')
         , name='reset_password_done'),

    path('reset/<uidb64>/<token>', auth_views.PasswordResetConfirmView.as_view(template_name=
                                                                               'users/password_reset_confirm.html'),
         name='reset_password_confirm'),

    path('reset_password_complete', auth_views.PasswordResetCompleteView.as_view(template_name=
                                                                                 'users/password_reset_complete.html'),
         name='reset_password_complete'),

    path('user_logout', views.user_logout, name='user_logout'),

    path('change_password/',
         auth_views.PasswordChangeView.as_view(template_name='users/change_password.html'), name='change_password'),

    path('password_change_done/',
         auth_views.PasswordChangeView.as_view(template_name='users/password_change_done.html'),
         name='password_change_done'),

    path('account_del/', views.account_del, name='account_del'),

    path('file_user', views.user_data_file, name="file_user")
]

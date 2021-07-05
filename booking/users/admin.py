from django.contrib import admin
from .models import User, EmailSender
from django.core.mail import send_mass_mail
import smtplib


admin.site.register(User)


class EmailSenderAdmin(admin.ModelAdmin):
    actions = ['send_email']

    @admin.action(description='Send mass email')
    def send_email(self, request, queryset):
        for obj in queryset:
            lst = obj.adresses
            email_list = list(lst.replace(' ', '').split(','))
            subject = obj.subject
            msg = obj.text
            t = (subject, msg, 'from@example.com', email_list)
            send_mass_mail((t,), fail_silently=False, auth_user=None, auth_password=None, connection=None)




admin.site.register(EmailSender, EmailSenderAdmin)

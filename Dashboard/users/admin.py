from django.contrib import admin
from .models import Profile

class ProfileAdmin(admin.ModelAdmin):
    list_display = ("username","first_name" , "last_name", "email","phone_number", "account_balance",)

admin.site.register(Profile,ProfileAdmin)
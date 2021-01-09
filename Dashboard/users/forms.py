from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class NewUserForm(UserCreationForm):
    email = forms.EmailField(required=True)
    phone_number = forms.IntegerField(required=True)
    account_balance = forms.IntegerField(required=True)
    first_name = forms.CharField(max_length=32, required=True)
    last_name = forms.CharField(max_length=32, required=True)

    class Meta:
        model = User
        fields = ("username", "email", "password1", "password2",
                  "phone_number", "account_balance", "first_name", "last_name")

"""    def save(self, commit=True):
        user = super(NewUserForm, self).save(commit=False)
        user.email = self.cleaned_data['email']
        user.phone_number = self.cleaned_data['phone_number']
        user.account_balance = self.cleaned_data['account_balance']
        user
        if commit:
            user.save()
        return user"""

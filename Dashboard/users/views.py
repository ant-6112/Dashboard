from django.shortcuts import render, redirect
from .forms import NewUserForm
from django.contrib.auth import login, authenticate, logout
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm
from .models import Profile
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse

def index(request):
    if not request.user.is_authenticated:
        return HttpResponseRedirect(reverse("users:login"))
    return render(request, "users/userprofile.html",{"Profile" : Profile.objects.all()})

def main(request):
    return render(request, "users/main0.html", {
        "Profile": Profile.objects.all()
    })

def register_user(request):
    if request.method == "POST":
        form = NewUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            profile = user.profile
            profile.username = form.cleaned_data.get('username')
            profile.first_name = form.cleaned_data.get('first_name')
            profile.last_name = form.cleaned_data.get('last_name')
            profile.email = form.cleaned_data.get('email')
            profile.phone_number = form.cleaned_data.get(
                'phone_number')
            profile.account_balance = form.cleaned_data.get(
                'account_balance')
            profile.save()
            user.save()
            login(request, user)
            messages.success(request, "Registration successful.")
            return redirect("users:homepage")
        messages.error(
            request, "Unsuccessful registration. Invalid information.")
    form = NewUserForm
    return render(request=request, template_name="users/register.html", context={"register_form": form})


def login_user(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return HttpResponseRedirect(reverse("users:index"))
            else:
                return render(request, "users/login.html", {
                "message": "Invalid credentials."
                })
                messages.error(request, "Invalid username or password.")
        else:
            return render(request, "users/login.html", {
            "message": "Invalid credentials."
            })
            messages.error(request, "Invalid username or password.")
    form = AuthenticationForm()
    return render(request=request, template_name="users/login.html", context={"login_form": form})


def logout_user(request):
    logout(request)
    return render(request, "users/login.html", {
        "message": "Logged out."
    })


def homepage(request):
    return render(request, "users\homepage.html")



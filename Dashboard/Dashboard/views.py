from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect

def homepage(request):
    return render(request, "users\homepage.html")
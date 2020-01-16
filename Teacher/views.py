from django.shortcuts import render

# Create your views here.


def home(request):
    return render(request, "Teacher/index.html")


def login(request):
    return render(request, "Teacher/login.html")


def register(request):
    return render(request, "Teacher/register.html")

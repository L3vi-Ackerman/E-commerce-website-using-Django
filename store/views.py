from django.shortcuts import render
from .models import Product
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages


def Home(request):
    products = Product.objects.all()
    return render(request, "home.html", {"products": products})


def About(request):
    return render(request, "about.html", {})


def login_user(request):
    return render(request, "login.html", {})


def logout_user(request):
    pass

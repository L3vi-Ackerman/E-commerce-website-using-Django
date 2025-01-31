from django.urls import path, include
from . import views

urlpatterns = [
    path("", views.Home, name="home"),
    path("about", views.About, name="about"),
    path("login/", views.login_user, name="login"),
    path("logout/", views.logout_user, name="logout"),
    path("register/", views.register_user, name="register"),
]

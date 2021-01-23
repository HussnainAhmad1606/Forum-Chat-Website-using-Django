from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("messages/", views.UserMessages, name="messages"),
    path("signup/", views.signup, name="signup"),
    path("login/", views.handleLogin, name="login"),
    path("logout/", views.logoutUser, name="logout")



]

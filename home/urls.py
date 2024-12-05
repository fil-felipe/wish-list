from django.urls import path, include
from django.contrib.auth import views as auth_views
from . import views

app_name = "home"
urlpatterns = [
    path("", include("django.contrib.auth.urls")),
    path("", views.home, name="home"),
    path("register/", views.register, name="register"),
    path("users/", views.get_users, name="users"),
    path("user_info", views.user_info, name="user_info"),
]

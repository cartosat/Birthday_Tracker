from django.shortcuts import redirect
from django.urls import path
from . import views

app_name = 'UserAuth'
urlpatterns = [
    path('register/', views.registerUser, name="register"),
    path('', views.loginUser, name="login"),
    path('login/', views.loginUser, name="login"),
    path('logout/', views.logoutUser, name="logout"),
    path('password_reset/', views.passwordReset, name="passwordReset"),

]

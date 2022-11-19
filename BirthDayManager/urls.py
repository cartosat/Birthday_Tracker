from django.urls import path
from . import views

app_name = 'BirthDayManager'
urlpatterns = [
    path('', views.home, name="home"),
    path('home/', views.home, name="home"),
    path('profile/', views.profile, name="profile"),
    path('edit_profile/', views.edit_profile, name="edit_profile"),
    path('profile/<str:pk>', views.friend_profile, name="friend_profile"),
    path('edit_friend/<str:pk>', views.edit_friend, name="edit_friend"),
    path('add_friend/', views.add_friend, name="add_friend"),

]

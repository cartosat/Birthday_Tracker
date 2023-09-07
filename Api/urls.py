from django.urls import path
from . import views
from Api.views import InitialApi
app_name = 'Api'
urlpatterns = [
    path('greet/', InitialApi.as_view(), name="home"),
]

from django.shortcuts import render
from django.http import JsonResponse

# Create your views here.
def home(request):
    data = {
        'message': 'Hello to API home',
    }
    return JsonResponse(data) 
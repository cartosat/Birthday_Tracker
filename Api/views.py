from django.shortcuts import render
from django.http import JsonResponse
from rest_framework.views import APIView
from rest_framework.generics import GenericAPIView
from rest_framework.response import Response

# Create your views here.
class InitialApi(APIView):
    def get(self, request):
        data = {
            'message': 'Hello to API home',
        }
        return JsonResponse(data)
    
    def post(self, request):
        user_name = request.data.get("user_name")
        data = {
            'message': f'Hello {user_name} !!!',
        }
        return JsonResponse(data)
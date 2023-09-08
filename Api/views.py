from django.shortcuts import render
from django.http import JsonResponse
from rest_framework.views import APIView

# Create your views here.
class InitialApi(APIView):
    def get(self, request):
        data = {
            'message': 'Hello to API home',
        }
        return JsonResponse(data)
    
    def post(self, request):
        user_name = request.POST.get("user_name")
        data = {
            'message': f'Hello {user_name} !!!',
        }
        return JsonResponse(data)
    
    def put(self, request):
        user_name = request.data.get("user_name")
        data = {
            'message': f'Hello {user_name} !!!',
        }
        return JsonResponse(data)
    
    def delete(self, request):
        user_name = request.data.get("user_name")
        data = {
            'message': f'Hello {user_name} !!!',
        }
        return JsonResponse(data)
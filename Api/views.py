from django.shortcuts import render
from django.http import JsonResponse
from rest_framework.views import APIView
from drf_spectacular.utils import extend_schema, extend_schema_view, OpenApiParameter

# Create your views here.
@extend_schema_view(
    post=extend_schema(
        parameters=[
            OpenApiParameter(name='user_name', description='User name', type=str),
        ]
    )
)
class InitialApi(APIView):
    def get(self, request):
        data = {
            'message': 'Hello to API home',
        }
        return JsonResponse(data)
    
    def post(self, request):
        user_name = request.query_params.get('user_name')
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
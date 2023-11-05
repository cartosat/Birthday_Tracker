from django.shortcuts import render
from django.http import JsonResponse, HttpResponse
from rest_framework.views import APIView
from drf_spectacular.utils import extend_schema, extend_schema_view, OpenApiParameter
from UserAuth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication
from itertools import chain
from BirthDayManager.models import FriendDetail, DefaultFriend
from django.core import serializers
from django.db.models import Q

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

class Home(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]
    
    def get(self, request):
        search_query = ""
        if request.GET.get("search_query"):
            search_query = request.GET.get("search_query")

        # Showing default friends only if `show_default_friends` checkbox is checked in profile section
        if request.user.show_default_friends:

            FriendSearchList = FriendDetail.objects.filter(member_friend=request.user.id).filter(Q(first_name__icontains=search_query) | 
                Q(last_name__icontains=search_query) | Q(phone_number__icontains=search_query) |
                Q(city__icontains=search_query) | Q(email__icontains=search_query)|
                Q(social_instagram__icontains=search_query))

            DefaultSearchList = DefaultFriend.objects.filter(Q(first_name__icontains=search_query) | 
                Q(last_name__icontains=search_query) | Q(phone_number__icontains=search_query) |
                Q(city__icontains=search_query) | Q(email__icontains=search_query)|
                Q(social_instagram__icontains=search_query))

            json_data = serializers.serialize('json', list(chain(FriendSearchList, DefaultSearchList)))

        else:

            FriendSearchList = FriendDetail.objects.filter(Q(first_name__icontains=search_query) | 
                Q(last_name__icontains=search_query) | Q(phone_number__icontains=search_query) |
                Q(city__icontains=search_query) | Q(email__icontains=search_query)|
                Q(social_instagram__icontains=search_query))
        
            json_data =  serializers.serialize('json', list(chain(FriendSearchList)))

        return HttpResponse(json_data)

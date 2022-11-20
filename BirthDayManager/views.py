from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from .forms import FriendDetailForm, UpdateFriendForm
from UserAuth.models import CustomUser
from UserAuth.forms import UserUpdateForm
from .models import FriendDetail, DefaultFriend
from itertools import chain
import operator


# Create your views here.
def searchProfiles(request):
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

        return list(chain(FriendSearchList, DefaultSearchList)), search_query

    else:

        FriendSearchList = FriendDetail.objects.filter(Q(first_name__icontains=search_query) | 
            Q(last_name__icontains=search_query) | Q(phone_number__icontains=search_query) |
            Q(city__icontains=search_query) | Q(email__icontains=search_query)|
            Q(social_instagram__icontains=search_query))
    
        return list(chain(FriendSearchList)), search_query

@login_required(login_url="auth/login")
def home(request):
    
    FriendList, search_query = searchProfiles(request)

    context = {
            "username" : request.user.first_name,

            "data" : sorted(FriendList, key=operator.attrgetter('remaining_days')),

            "search_query": search_query
        }

    return render(request, 'home.html', context)



@login_required(login_url="/auth/login")
def profile(request):
    userData = CustomUser.objects.filter(email=request.user.email)
    context = {
        "username" : request.user.first_name,
        "data" : userData
    }
    return render(request, 'my_profile.html', context)


@login_required(login_url="/auth/login")
def edit_profile(request):
    userData = CustomUser.objects.filter(email=request.user.email)
    context = {
        "username" : request.user.first_name,
        "data" : userData
    }

    if request.method == 'POST':
        profile_form = UserUpdateForm(request.POST, request.FILES, instance=request.user)

        if profile_form.is_valid():
            profile_form.save()
            return redirect("BirthDayManager:profile")
    
    return render(request, 'edit_profile.html', context)

@login_required(login_url="/auth/login")
def add_friend(request):
    profile = request.user
    form = FriendDetailForm(instance=profile)

    if request.method == "POST":
        form = FriendDetailForm(request.POST, request.FILES)
        if form.is_valid():
            obj = form.save(commit = False)
            # I am mapping primary key from User table to foreign key in friend table.
            # We can only map primary key defined in table 1 to foreign key in table 2.
            # refer models file for more.
            obj.member_friend = request.user
            obj.save()
            messages.success(request, "User Added Succesfully !")
            return redirect("BirthDayManager:home")

    context = {"form": FriendDetailForm(), "username" : request.user.first_name}
    return render(request, 'add_friend.html', context)


@login_required(login_url="/auth/login")
def friend_profile(request, pk):

    FriendData = FriendDetail.objects.filter(id=pk).values()

    # FriendData will empty if clicked on default user.
    if not FriendData:
        FriendData = DefaultFriend.objects.filter(id=pk).values()
        
    context = {
        "username" : request.user.first_name,
        "data" : FriendData
    }
    return render(request, 'friend_profile.html', context)


@login_required(login_url="/auth/login")
def edit_friend(request, pk):
    friendData = FriendDetail.objects.filter(id = pk)
    f_instance =  FriendDetail.objects.get(pk=pk)
    context = {
        "username" : request.user.first_name,
        "data" : friendData
    }
    if request.method == 'POST':
        f_instance =  FriendDetail.objects.get(pk=pk)
        friend_update_form = UpdateFriendForm(request.POST, request.FILES, instance=f_instance)

        if friend_update_form.is_valid():
            friend_update_form.save()
            return redirect("BirthDayManager:home")

    return render(request, 'edit_friend_profile.html', context)

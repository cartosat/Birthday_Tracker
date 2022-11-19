from django.http import HttpResponse
from django.contrib import messages
from django.shortcuts import redirect, render
from .forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout

# Create your views here.


def registerUser(request):
    form = UserCreationForm()
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "User registered Succesfully !")
            return redirect('UserAuth:login')

        else:
            messages.error(request, "Error occurred during registration !")
            return redirect("UserAuth:register")

    context = {"page": "register", "form": form}
    return render(request, "register.html", context)


def loginUser(request):
    page = "login"
    if request.user.is_authenticated:
        return redirect("BirthDayManager:home")

    if request.method == "POST":
        email = request.POST["email"]
        password = request.POST["password"]
        try:
            user = User.objects.get(email=email)
        except:
            messages.error(request, "User not exists")

        user = authenticate(request, email=email, password=password)
        # returns None if password not matched
        if user is not None:
            # It will create session for this user in database
            login(request, user)
            # check inspect --> application --> cookies
            return redirect('BirthDayManager:home')
        else:
            messages.error(request, "Invalid username or password")

    context = {"page": page}

    return render(request, 'login.html', context)


def logoutUser(request):
    logout(request)  # This will delet tha session from table
    messages.error(request, "User logged out")
    return redirect("UserAuth:login")


def passwordReset(request):
    return render(request, "password_reset.html")

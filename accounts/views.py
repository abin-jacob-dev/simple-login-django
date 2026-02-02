from django.shortcuts import render,redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.views.decorators.cache import never_cache
from django.http import HttpResponse

# Create your views here.
@never_cache
@login_required
def home(request):
    return render(request, "accounts/home.html", {"user": request.user})

@never_cache
def login_view(request):
    if request.user.is_authenticated:
        return redirect("home")
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            return redirect('home')
        else:
            return render(
                request,
                "accounts/login.html",
                {"error": "Invalid username or password"},
            )
    return render(request, "accounts/login.html")

@never_cache
def logout_view(request):
    logout(request)
    return redirect("login")

def name_view(request):
    return render(request,'accounts/name.html',{"message":'Abin Jacob'})

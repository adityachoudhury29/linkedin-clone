from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout
from django.db import IntegrityError
from django.urls import reverse
from .models import User, posts

# Create your views here.

def login_view(request):
    if request.method == "POST":

        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse("index"))
        else:
            return render(request, "lprofile/login.html", {
                "message": "Invalid username and/or password."
            })
    else:
        return render(request, "lprofile/login.html")


def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse("index"))


def register(request):
    if request.method == "POST":
        username = request.POST["username"]
        email = request.POST["email"]

        password = request.POST["password"]
        confirmation = request.POST["confirmation"]
        if password != confirmation:
            return render(request, "lprofile/register.html", {
                "message": "Passwords must match."
            })

        try:
            user = User.objects.create_user(username, email, password)
            user.save()
        except IntegrityError:
            return render(request, "lprofile/register.html", {
                "message": "Username already taken."
            })
        login(request, user)
        return HttpResponseRedirect(reverse("index"))
    else:
        return render(request, "lprofile/register.html")
    
def index(request):
    posts2=posts.objects.all()
    return render(request,'lprofile/index.html',{
        'posts1':posts2
    })

def profile1(request):
    return render(request,'lprofile/profile1.html')

def create(request):
    if request.method=='GET':
        return render(request,'lprofile/create.html')
    else:
        desc=request.POST["desc"]
        user=request.user
        newpost=posts(owner=user,desc=desc)
        newpost.save()
        posts1=posts.objects.all()
        return render(request,'lprofile/index.html',{
            'posts1':posts1
        })
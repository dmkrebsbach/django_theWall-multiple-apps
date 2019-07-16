from django.shortcuts import render, redirect
import bcrypt
from apps.logAndReg.models import User
from apps.theWall.models import Message, Comment 
from django.contrib import messages
import datetime

def index(request):
    
    return render(request, "logAndReg/index.html")

def registration(request):
    if request.method == "POST":

        errors = User.objects.registrationValidator(request.POST)
        if len(errors) > 0:
            for key, value in errors.items():
                messages.error(request, value)
            return redirect("/")

        newUser = User.objects.create(
            firstName = request.POST["firstName"],
            lastName = request.POST["lastName"],
            email = request.POST["email"],
            birthDate = request.POST["birthDate"],
            password = bcrypt.hashpw(request.POST["password"].encode(), bcrypt.gensalt()),
        )
        newUser.save()
        request.session["id"]=newUser.id
        request.session["firstName"]=newUser.firstName
    return redirect("/thewall/success")

def login(request):
    if request.method == "POST":

        errors = User.objects.loginValidator(request.POST)
        if len(errors) > 0:
            for key, value in errors.items():
                messages.error(request, value)
            return redirect("/")

        user = User.objects.get(email=request.POST['loginEmail'])
        if bcrypt.checkpw(request.POST['password'].encode(), user.password.encode()):
            print("User Password Matches")
            request.session["id"]=user.id
            request.session["firstName"]=user.firstName
            return redirect("/thewall/success")
        else:
            print("User Password Match Fails")
            return redirect("/")



def logout(request):
    request.session.clear()
    return redirect("/")
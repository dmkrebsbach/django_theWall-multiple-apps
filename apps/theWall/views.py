from django.shortcuts import render, redirect
import bcrypt
from apps.logAndReg.models import User
from apps.theWall.models import Message, Comment 
from django.contrib import messages
import datetime
import pytz

def success(request):

    if "id" in request.session:
        context = {
            'user':User.objects.get(id=request.session['id']),
            'postedMessages':Message.objects.all(),
            'postedComments':Comment.objects.all(),
        }
        print("user is in session")
        return render(request, 'theWall/wall.html', context)
    return redirect ("/")

def add_message(request):
    print("add message initiated")
    if request.method == "POST":
        thisUser = User.objects.get(id=request.session["id"])
        print(request.session['id'])
        newMessage = Message.objects.create(
            content = request.POST["add_message"],
            user = thisUser,
        )
        newMessage.save()
    return redirect("/thewall/success")

def comment(request, messageId):
    print("add comment initiated")
    if request.method =="POST":
        thisUser = User.objects.get(id=request.session["id"])
        thisMessage = Message.objects.get(id=messageId)
        newComment = Comment.objects.create(
            content = request.POST['userComment'],
            user = thisUser,
            message = thisMessage,
        )
        newComment.save()
    return redirect("/thewall/success")

def delete(request, messageId):
    cutoff = pytz.utc.localize(datetime.datetime.now() - datetime.timedelta(minutes = 30))
    if Message.objects.get(id = messageId).createdAt < cutoff:
        messages.error(request, "Message created more than 30 minutes ago, cannot be removed")
        return redirect("/thewall/success")

    Message.objects.get(id = messageId).delete()

    return redirect("/thewall/success")

def logout(request):
    request.session.clear()
    return redirect("/")
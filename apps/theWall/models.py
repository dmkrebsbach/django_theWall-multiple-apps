from django.db import models
from validate_email import validate_email   
import bcrypt                               
import datetime                            
import re
from apps.logAndReg.models import User                              

class Message(models.Model):
    content = models.TextField()
    user = models.ForeignKey(User, related_name = 'messages')
    createdAt = models.DateTimeField(auto_now_add=True)
    updatedAt = models.DateTimeField(auto_now_add=True)

class Comment(models.Model):
    content = models.TextField()
    message = models.ForeignKey(Message, related_name = "comments")
    user = models.ForeignKey (User, related_name = "comments")
    createdAt = models.DateTimeField(auto_now_add=True)
    updatedAt = models.DateTimeField(auto_now_add=True)
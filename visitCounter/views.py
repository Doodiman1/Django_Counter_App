from django.http import HttpResponse
from django.contrib.auth import authenticate
from django.shortcuts import render, get_object_or_404
from django.db.models import F
from django.contrib.auth.models import User
from .models import Visit
# Create your views here.

def index(request):
    visitor = Visit.objects.filter(username = 'Test')
    visitor.update(count=F("count") + 1)
    context = { "visitor" : visitor }
    return render(
            request, 
            "visitCounter/index.html",
            context
            )

def createUser(request):
    #newUser = User.objects.create_user()
    #context = {"user" : user }
    return render(
            request,
            "registration/new_user.html",
            #context
            )

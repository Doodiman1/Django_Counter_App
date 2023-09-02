from django.contrib.auth import authenticate
from django.shortcuts import render
from django.db.models import F
from django.views import generic
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from .models import Visit


def index(request):
    visitor = Visit.objects.filter(username = 'Test')
    visitor.update(count=F("count") + 1)
    context = { "visitor" : visitor }
    return render(
            request, 
            "visitCounter/index.html",
            context
            )

class createUser(generic.CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy("login")
    template_name = "registration/create_user.html"


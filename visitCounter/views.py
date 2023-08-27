from django.shortcuts import render, get_object_or_404
from .models import Visit
# Create your views here.

def index(request):
    visitor = Visit.objects.all()
    context = { "visitor": visitor }
    return render(
            request, 
            "visitCounter/index.html",
            context
            )

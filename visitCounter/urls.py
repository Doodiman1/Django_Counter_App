from django.urls import path, include

from . import views

urlpatterns = [
        path("", views.index, name = "index"),
        path("accounts/", include('django.contrib.auth.urls')),
        path("create_user/", views.createUser.as_view(), name = "create_user"),
        ]

from django.contrib import admin
from django.urls import path
from . import views

app_name="logins"
urlpatterns = [
    path("", views.create, name="create")
]

from django.contrib import admin
from django.urls import path
from . import views

from django.views.generic import TemplateView

app_name="logins"
urlpatterns = [
    path("", views.create, name="create")
]

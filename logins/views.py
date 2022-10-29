from django.shortcuts import render, redirect
from .models import User

from rest_framework.response import Response
from rest_framework.views import APIView

# Create your views here.

def create(request):
    if request.method == "POST":
        email = request.POST["email"]
        
        User.objects.create(email=email)
        return redirect("/")
    
    return render(request, template_name = "home.html")
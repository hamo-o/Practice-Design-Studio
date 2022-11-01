from django.shortcuts import render, redirect
from .models import User

# Create your views here.

def create(request):
    if request.method == "POST":
        email = request.POST["email"]
        
        user = User.objects.create(email=email)
        print(user)
        user.save()
        return redirect("/")
    
    return render(request, template_name = "home.html")
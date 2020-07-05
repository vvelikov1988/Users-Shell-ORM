from django.shortcuts import render, HttpResponse, redirect
from .models import User

def home(request):
    userdata = {
        "user_data": User.objects.all()
    }
    return render (request, "index.html", userdata)

def results(request):
    User.objects.create(
        first_name=request.POST['fname'],
        last_name=request.POST['lname'],
        email=request.POST['email'],
        age=request.POST['age']
)
    return redirect('/')
    
# Create your views here.

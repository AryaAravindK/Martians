from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import login,logout
from django.contrib import messages
from django.http import HttpResponse

# Create your views here.
def register(request):
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        email = request.POST['email']
        password1 = request.POST['password1']
        password2 = request.POST['password2']
        
        if password1 == password2:
            if User.objects.filter(username=username).exists():
                messages.error(request, 'Username already exists')
            elif User.objects.filter(email=email).exists():
                messages.error(request, 'Email already registered')
            else:
                user = User.objects.create_user(username=username, first_name=first_name, last_name=last_name, email=email, password=password1)
                user.save()
                login(request,user)
                print("User saved")
                
                return redirect('/')
        else:
            messages.error(request, 'Passwords do not match')
        return render(request,'register.html')

    else:
        return render(request, 'register.html')
    
    
def logout_handler(request):
    logout(request)
    return redirect('/')
    



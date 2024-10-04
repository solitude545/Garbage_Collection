from django.shortcuts import render,redirect
from.models import *
from django.contrib import messages
from django.contrib.auth import login as auth_login,authenticate
# Create your views here.
def home(request):
    return render(request,'home.html')
def login_view(request):
    if request.method == 'POST':
        username = request.POST.get("username")
        password = request.POST.get("password")
        
        # Authenticate the user
        user = authenticate(request, username=username, password=password)
        print(user)

        if user is not None:
            # Log the user in
            auth_login(request, user)

            # Redirect to the desired page after successful login
            return render(request, 'base.html',{'data':user})

        else:
            # Invalid credentials
            return render(request, 'login.html', {'error': 'Invalid username or password'})

    return render(request, 'login.html')
def register(request):
    if request.method=='POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        password = request.POST.get('password') 
        cpassword = request.POST.get('cpassword')
        if password != cpassword: 
            messages.error(request, "Passwords do not match")
            return render(request,'login.html')
        x=User(username=username)
        x.set_password(password)
        x.save()
        UserProfile.objects.create(user=x,phone=phone,email=email)
        messages.success(request, "Registration successful. You can now log in.")
        return redirect('login_view') 
    else:
        return render(request, 'login.html')


def base_view(request):
    return render(request, 'base.html')

def bio_view(request):
    return render(request, 'bio.html')
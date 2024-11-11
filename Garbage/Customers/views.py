from django.shortcuts import render,redirect
from.models import *
from django.contrib import messages
from django.contrib.auth import login as auth_login,authenticate
import plotly.express as px
import pandas as pd
from django.http import HttpResponseRedirect,HttpResponse


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
def nonbio_view(request):
    return render(request, 'nonbio.html')
def haz_view(request):
    return render(request, 'haz.html')
def conord_view(request):
    return render(request, 'conforder.html')
def order_view(request):
    return render(request, 'orders.html')


def map_view(request):
    if request.method == "POST":
        name = request.POST.get('name')
        type = request.POST.get('wasteType')
        weight = request.POST.get('weight')
        ord = {
            'name' : name,
            'type' : type,
            'weight' : weight
        }
    return render(request, 'map.html',{'data':ord})

def submit_location(request):
    if request.method == "POST":
       
        name = request.POST.get('name')
        type = request.POST.get('type')
        weight = request.POST.get('weight')
        location = request.POST.get('location')
        ord_upd ={
            'name': name,
            'type' : type,
            'weight' : weight,
            'location' : location
        }
        print(ord_upd)
        
        
    return render(request, 'conforder.html', {'data': ord_upd})

    
def payment_view(request):
        if request.method == "POST":
            fullname = request.POST.get('name')
            wastetype = request.POST.get('type')
            Weight = request.POST.get('weight')
            location = request.POST.get('location')
            query = Order(fullname=fullname,wastetype=wastetype,wasteweight=Weight,location=location)
            query.save()
        return render(request, 'payment.html')
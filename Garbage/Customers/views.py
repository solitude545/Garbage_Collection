from django.shortcuts import render,redirect
from.models import user_reg
from django.contrib import messages
from django.contrib.auth import login as auth_login
# Create your views here.
def home(request):
    return render(request,'home.html')
def login_view(request):
    if request.method=='POST':
        username=request.POST["username"]
        password=request.POST["password"]
        res=user_reg.objects.filter(username=username,password=password)
        # res=logins.authenticate(username=username, password=password)
        print(res) 
        if res.exists():
            res1=user_reg.objects.get(username=username)
            return render(request, 'base.html')
        else:
            return render(request,'login.html')
    else:
        return render(request,'login.html')

def register(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        password = request.POST.get('password') 
        cpassword = request.POST.get('cpassword')

        if password != cpassword:
            messages.error(request, "Passwords do not match")
            return render(request,'login.html')

        if user_reg.objects.filter(email=email).exists():
            messages.error(request, "Email already exists")
            return render(request,'login.html')

        if user_reg.objects.filter(username=username).exists():
            messages.error(request, "Username already exists")
            return render(request,'login.html')

      
        user = user_reg(username=username, email=email, phone=phone, password=password)
        user.save()

        messages.success(request, "Registration successful. You can now log in.")
        return redirect('login_view') 

    return render(request, 'login.html')  


def base_view(request):
    return render(request, 'base.html')
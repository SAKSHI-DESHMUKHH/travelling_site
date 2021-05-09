from django.shortcuts import render,redirect
from django.contrib.auth.models import User,auth
from django.contrib import messages
from django.contrib.auth import logout


# Create your views here.
def user_register(request):
    if request.method == 'POST':
        firstname=request.POST['firstname']
        lastname=request.POST['lastname']
        username=request.POST['username']
        email=request.POST['email']
        password=request.POST['password']
        password2=request.POST['password2']
        if password==password2:
            if User.objects.filter(username=username).exists():
                messages.error(request,'Username already registered')
                return redirect('register')
                
            else:
                if User.objects.filter(email=email).exists():
                    messages.error(request,'Email already registered')
                    return redirect('register')
                    
                else:
                    user=User.objects.create_user(first_name=firstname, last_name=lastname, username=username, email=email, password=password)
                    user.save()
                    messages.success(request,'Account Created successfully')
                    return redirect('login_page')
        else:
            messages.error(request,'Password Mismatch')
            return redirect('register')
    else:
        return render(request,'user/register.html')

def user_login(request):
    if request.method=='POST':
        username=request.POST['username']
        password=request.POST['password']
        user=auth.authenticate(username=username,password=password)
        if (user):
            auth.login(request,user)
            return redirect('/')
        else:
            messages.info(request,'Invalid Credentials')
            return render(request,'user/login.html')
    else:
        return render(request,'user/login.html')
    # if request.method=='POST':
    #     username=request.POST['username']
    #     password=request.POST['password']
    #     user=auth.authenticate(username=username, password=password)
    #     if user is not None:
    #         auth.login(request, user)
    #         messages.error(request, 'you are logged in')
    #         return redirect('dashboard')
    #     else:
    #         messages.error(request, 'invalid credentials')
    #         return redirect('login_page')

def user_logout(request):
    logout(request)
    return redirect('home')

def dashboard(request):
    pass
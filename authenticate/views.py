from django.shortcuts import redirect, render
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
global o1,o2,o3,o4
o1,o2,o3,o4=0,0,0,0

# Create your views here.
def home(request):
    return render(request, "authenticate/signup.html")


def signup(request):
    
    if request.method=="POST":
        username=request.POST['username']
        password=request.POST['pass']
        
        
        if (username,)in (User.objects.all().values_list('username')):
            messages.error(request, "This username is already taken")
            
        else:
            myuser=User.objects.create_user(username=username,password=password)
            myuser.save()
            messages.success(request,"Your Account has been successfully created!")
            
       #return redirect("signin")
        


    return render(request,"authenticate/signup.html")


def signin(request):
    if request.method=="POST":
        username=request.POST['username']
        password=request.POST['pass']
        print(username)
        user=authenticate(username=username,password=password)#returns none if user is not authed
        if user is not None:
            login(request,user)
            username=user.get_username()
            return render(request,"authenticate/index.html",{'uname':username})
        else:
            messages.error(request,"Username or Password Incorrect!")
         
    return render(request,"authenticate/signin.html")

def signout(request):
    logout(request)
    messages.success(request,"Logout Succesfull")
    return redirect("home")

def voting(request):
    global o1,o2,o3,o4
    if request.method=="POST":
            try:
                request.POST['opt-1']
                o1=o1+1
                return render(request,"authenticate/voting.html",{'p1':o1,'p2':o2,'p3':o3,'p4':o4,})
            except:
                pass

            try:
                request.POST['opt-2']
                o2=o2+1
                return render(request,"authenticate/voting.html",{'p1':o1,'p2':o2,'p3':o3,'p4':o4,})
            except:
                pass

            try:
                request.POST['opt-3']
                o3=o3+1
                return render(request,"authenticate/voting.html",{'p1':o1,'p2':o2,'p3':o3,'p4':o4,})
            except:
                pass

            try:
                request.POST['opt-4']
                o4=o4+1
                return render(request,"authenticate/voting.html",{'p1':o1,'p2':o2,'p3':o3,'p4':o4,})
            except:
                pass
            
            

        
        
    return render(request,"authenticate/voting.html")
def out(request):
    return render(request,"authenticate/out.html")
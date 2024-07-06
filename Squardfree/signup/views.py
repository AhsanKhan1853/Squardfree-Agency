from django.shortcuts import HttpResponse
from django.shortcuts import render,redirect
from .models import SignUp
from django.contrib.auth.models import auth,User
from django.contrib import messages
# Create your views here.
def booking(request):
    user = SignUp.objects.all()
   
    return render(request,'contact.html',{'user': user})

def signUP(request):
    if request.method == "POST":
        
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        password1 = request.POST['password1']
        password2 = request.POST['password2']
        email = request.POST['email']
        if password1 == password2:

            if User.objects.filter(username=username).exists():
                messages.info(request,"Username is Taken")
                return redirect("booking")
            
            elif User.objects.filter(email= email).exists():
                messages.info(request,"Email Already Exists. If That's Yours Login Instead")
                return redirect("booking")
            
            else:
                user = User.objects.create_user(username=username, password=password1, email=email, first_name= first_name, last_name= last_name)
                user.save();
                print("hogaya..")
                auth.login(request,user)
                return redirect("/")
        else:
            messages.info(request,"Passwords are not same")
            return redirect("booking")
    else:
        return HttpResponse("helol")
    
def login(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username, password= password)
        if user is not None:
            auth.login(request,user)
            return redirect("/")
        else:
            messages.info(request,"User is not avalaible")
            return redirect("login")
    else:
        return render(request,'login.html')
    
def logout(request):
    auth.logout(request)
    return redirect("/")
def about(request):

    return render(request,'about.html')

def whatwedo(request):

    return render(request,'do.html')

def portfolio(request):

    return render(request,'portfolio.html')
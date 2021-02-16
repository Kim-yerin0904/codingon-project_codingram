from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import redirect
from .models import User

# Create your views here.

def login_view(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST["password"]
        user = authenticate(username=username, password=password)
        if user is not None:
            print ("인증성공")
            login(request, user)
            return render(request, "users/login.html")
            return render(request, "blog.html",{'username':username})
        else:
            print("인증실패")
            return render(request)
    else:
        return render(request, "users/login.html")
    
    

def logout_view(request):
    logout(request)
    return redirect("user:login")


def signup_view(request):

    if request.method == "POST":
        print(request.POST)
        username = request.POST["username"]
        password = request.POST["password"]
        lastname = request.POST["lastname"]
        firstname = request.POST["firstname"]
        email = request.POST["email"]
        student_id = request.POST["student_id"]

        user = User.objects.create_user(username, email, password)
        user.last_name = lastname
        user.first_name = firstname
        user.student_id = student_id
        user.save()

        return login_view(request)
    else:
        return render(request, "users/signup.html")

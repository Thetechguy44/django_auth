from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import View

# Create your views here.

#this function is to view the home index page
def index(request):
    return render(request, 'auth/index.html')

# this is the signup function which is responsible for viewing the signup page and also handle signing up fuctionalities
def signup(request):
    if request.method == "POST":
        username = request.POST['username']
        fname = request.POST['fname']
        lname = request.POST['lname']
        email = request.POST['email']
        pass1 = request.POST['pass1']
        pass2 = request.POST['pass2']

        if User.objects.filter(username=username):
            messages.error(request, "username already exist")
            return redirect('signup')

        if User.objects.filter(email=email):
            messages.error(request, "email already exist")
            return redirect('signup')

        if len(username) > 10:
            messages.error(request, "username must be lessthan 10 characters")
            return redirect('signup')

        if pass1 != pass2:
            messages.error(request, "Passwords didn't match")
            return redirect('signup')

        if username.isalnum():
            messages.error(request, "Username must be Alpha-Numeric")
            return redirect('signup')

        newuser = User.objects.create_user(username, email, pass1)
        newuser.first_name = fname
        newuser.last_name = lname

        newuser.save()

        messages.success(request, "Your account has been successfully created")
        return redirect('/login')
    return render(request, 'auth/signup.html')

# this is the signin(login) function which is responsible for viewing the signin(login) page and also handle signing in or logging in fuctionalities
def signin(request):
    if request.method == "POST":
        username = request.POST['username']
        pass1 = request.POST['pass1']

        user = authenticate(username=username, password=pass1)

        if user is not None:
            login(request, user)
            return redirect('dashboard')
        else:
            messages.error(request, "Invalid credentials")
            return redirect('login')

    return render(request, 'auth/login.html')

# this is the signout(logout) function which is responsible for viewing the signout(logout) page and also handle signing out or login out fuctionalities
def signout(request):
    logout(request)
    messages.success(request, "Logout successfull")
    return redirect('home')

#this function is use to protect a function from guest. Only authenticated users can access it
@login_required 
def dashboard(request): # this is the dashboard function which is responsible for viewing the dashboard after authenticating
    return render(request, 'auth/dashboard.html')

# class ProtectedView(LoginRequiredMixin, View):
#     login_url = '/login/'
#     redirect_field_name = 'redirect_to'

#     def get(self, request):
#         return render(request, 'auth/dashboard.html')
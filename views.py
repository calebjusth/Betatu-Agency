from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import blog, team, user_profile
from .models import testimonial
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from .decorator import *

# Create your views here.
def home(request):
    staff = team
    testimonials = testimonial
    model = blog
    context = {
    'team_list': team.objects.all(), 
    'blog_list': blog.objects.all(), 
    'testimonial_list': testimonial.objects.all(),
    'user': request.user,
    }  
    return render(request, 'home.html', context)

#login page
@unauthenticated_user
def loginpage(request):  

    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('profiles')
        else:
            messages.error(request, 'login failed, password or user name is incorrect')


    return render(request, 'login.html') 



#sign up page
def signup(request):
    if request.method == "POST":
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        username = request.POST.get('username')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        gender = request.POST.get('gender')
        password = request.POST.get('password')
        password2 = request.POST.get('password2')

        new_user = User.objects.create_user(username, email, password)
        new_user.first_name = first_name
        new_user.last_name = last_name
        new_user.save()

        if len(phone) < 10:
            messages.warning(request, 'Phone number lenght is too short')
        if password != password2:
            messages.error(request, 'Error! passwords do not match')
        elif len(password) < 8:
            messages.error(request, 'password is too short')   
        else:
            return redirect('login')

    return render(request, 'signup.html')

#logout method
def logoutuser(request):
    logout(request)
    return redirect('login')

#blog page
def post(request):
    model = blog
    context = {'blog_list': model.objects.all(), 'user': request.user,}
    return render(request, 'blog.html', context)


#----------------------------app feathers section-------------------------------# 

@login_required
def proceed_page(request):
    
    context = {'user': request.user,}
    return render(request, 'procceed.html', context)

#account setup
@login_required
def profile_setup(request):
    store = user_profile.objects.all()
    if request.method == 'POST':
        profile_pic = request.POST.get('profile_pic')
        mobile = request.POST.get('mobile')
        profession = request.POST.get('profession')
        educational_background = request.POST.get('educational_background')
        experience = request.POST.get('experience')
        user_bio = request.POST.get('User_bio')
        user_cv = request.POST.get('cv')
        if profile_pic == '':
            messages.info(request, 'Please Upload a profile picture')
        if user_cv == "":
            messages.info(request, "Please add a CV")
        else:
            prof = user_profile(profile_pic=profile_pic, mobile=mobile, profession=profession, educational_background=educational_background, experience=experience, user_bio=user_bio, user_cv=user_cv)
            prof.save()
            return redirect('profiles')


    
    context = {'user': request.user,}
    return render(request, 'profile_setup.html', context)


#user profiles
@login_required
def profiles(request):
    context = {
    'user': request.user,
    'user_profile': user_profile.objects.all(),
    }
    return render(request, 'profiles.html', context)
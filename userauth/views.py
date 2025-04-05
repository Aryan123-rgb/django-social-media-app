from django.contrib.auth import authenticate, login
from django.shortcuts import redirect, render
from django.contrib.auth.models import User
from .models import Profile

def signup(request):
    try:
        if request.method == "POST":
            name = request.POST.get('name')
            email = request.POST.get('email')
            password = request.POST.get('password')
            image = request.POST.get('image')
            # print(name, email, password, image)
            user = User.objects.create_user(name, email, password)
            user.save()
            profile = Profile.objects.create(user=user, profile_image=image)
            profile.save()
            return redirect('/posts')
    except:
        ## error creating a user
        return redirect(request, 'signup.html')
    return render(request, 'signup.html')


def signin(request):
    if request.method == "POST":
        name = request.POST.get('name')
        password = request.POST.get('password')
        user = authenticate(username=name, password=password)
        
        if user is not None:
            login(request, user)
            return redirect('/posts')
    
    return render(request, 'signin.html')
    
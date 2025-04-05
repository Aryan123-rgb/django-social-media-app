from django.contrib.auth import authenticate, login
from django.shortcuts import redirect, render
from django.contrib.auth.models import User
from .models import Profile


def signup(request):
    if request.method == "POST":
        name = request.POST.get("name")
        email = request.POST.get("email")
        password = request.POST.get("password")
        profile_image = request.FILES.get("profile_image")
        # print('name', name)
        # print('email', email)
        # print('password', password)
        # print('profile_image', profile_image)
        try:
            user = User.objects.create_user(name, email, password)
            user.save()
            # print('user', user)
            profile = Profile.objects.create(user=user, profile_image=profile_image)
            profile.save()
            return redirect("/posts")
        except Exception as e:
            print("error", e)
            return render(request, "signup.html")
    return render(request, "signup.html")


def signin(request):
    if request.method == "POST":
        name = request.POST.get("name")
        password = request.POST.get("password")
        user = authenticate(username=name, password=password)

        if user is not None:
            login(request, user)
            return redirect("/posts")

    return render(request, "signin.html")

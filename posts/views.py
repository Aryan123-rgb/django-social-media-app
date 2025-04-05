from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .models import Posts, Profile

#Fetch all the posts
def get_posts(request):
    posts = Posts.objects.all()
    for idx, post in enumerate(posts):
        print('post ', idx + 1)
        print('post_content', post.post_content)
        print('post_image', post.post_image)
        print('created by', post.profile.user.username)
        print('profile_image', post.profile.profile_image.url)
        print()
    return render(request, 'posts.html', {'posts': posts})

# Create new post
@login_required(login_url="/auth/signin")
def create_posts(request):
    if request.method == "POST":
        post_content = request.POST.get('post_content')
        post_image = request.FILES.get('post_image')
        user = request.user
        try:
            profile = Profile.objects.filter(user=user).first()
            if not profile:
                print('No profile found for ', user.username)
                return redirect('/posts')
            
            posts = Posts.objects.create(
                post_content=post_content,
                post_image=post_image,
                profile=profile
            )
            return redirect('/posts')
        except Exception as e:
            print('error', e)
            return redirect('/posts')
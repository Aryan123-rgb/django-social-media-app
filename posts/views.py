from django.shortcuts import redirect, render, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .models import Posts, Profile, Comments


# Fetch all the posts
def get_posts(request):
    posts = Posts.objects.all()
    # for idx, post in enumerate(posts):
    #     print('post ', idx + 1)
    #     print('post_content', post.post_content)
    #     print('post_image', post.post_image)
    #     print('created by', post.profile.user.username)
    #     print('profile_image', post.profile.profile_image.url)
    #     print()
    user = request.user
    profile = Profile.objects.filter(user=user).first()
    print("profile", profile)
    data = {"posts": posts, "profile": profile}
    return render(request, "posts.html", {"data": data})


# Create new post
@login_required(login_url="/auth/signin")
def create_posts(request):
    if request.method == "POST":
        post_content = request.POST.get("post_content")
        post_image = request.FILES.get("post_image")
        user = request.user
        try:
            profile = Profile.objects.filter(user=user).first()
            if not profile:
                print("No profile found for ", user.username)
                return redirect("/posts")

            posts = Posts.objects.create(
                post_content=post_content, post_image=post_image, profile=profile
            )
            return redirect("/posts")
        except Exception as e:
            print("error", e)
            return redirect("/posts")


@login_required(login_url="/auth/signin")
def get_post(request, postId):
    post = get_object_or_404(Posts, id=postId)
    comments = Comments.objects.filter(post=post)
    # print('comments', comments)
    data = {
        'post': post,
        'comments': comments
    }
    return render(request, "post.html", {"data": data})


@login_required(login_url="/auth/signin")
def add_comments(request, postId):
    if request.method == "POST":
        comment_content = request.POST.get("comment_content")
        user = request.user
        profile = get_object_or_404(Profile, user=user)
        post = get_object_or_404(Posts, id=postId)
        # print("post", post)
        # print("profile", profile)
        try:
            comment = Comments.objects.create(
                comment_content=comment_content, profile=profile, post=post
            )
            comment.save()
        except Exception as e:
            print("error", e)
    return redirect(f"/posts/{postId}")

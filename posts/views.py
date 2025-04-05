from django.shortcuts import render
from .models import Posts

# Create your views here.
def get_posts(request):
    posts = Posts.objects.all()
    print('posts', posts)
    return render(request, 'posts.html')
from posts import views
from django.urls import path

urlpatterns = [
    path('', views.get_posts), 
    path('create_post', views.create_posts),
    path('<int:postId>', views.get_post),
    path('add_comments/<int:postId>', views.add_comments),
    path('generate_using_ai', views.generate_post_using_ai)
]

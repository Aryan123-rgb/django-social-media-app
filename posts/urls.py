from posts import views
from django.urls import path

urlpatterns = [
    path('', views.get_posts), 
    path('create_post', views.create_posts)
]

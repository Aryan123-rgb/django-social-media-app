from userauth import views
from django.urls import path

urlpatterns = [
    path('signup/', views.signup),
    path('signin/', views.signin)
]

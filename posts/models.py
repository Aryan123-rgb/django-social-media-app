from django.db import models
from userauth.models import Profile

# Create your models here.
class Posts(models.Model):
    title = models.CharField(max_length=500)
    content = models.CharField(max_length=1000)
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)
    post_image = models.ImageField(upload_to="/posts_imgs" , default='default.jpg')
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.title
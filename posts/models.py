from django.db import models
from userauth.models import Profile

# Create your models here.
class Posts(models.Model):
    post_content = models.CharField(max_length=1000)
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)
    post_image = models.ImageField(upload_to="posts_imgs/")
    created_at = models.DateTimeField(auto_now_add=True)
    like_count = models.IntegerField(default=0)
    
    def __str__(self):
        return self.post_content[:10]
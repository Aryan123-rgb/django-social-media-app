from django.db import models
from userauth.models import Profile


class Posts(models.Model):
    post_content = models.CharField(max_length=1000)
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)
    post_image = models.ImageField(upload_to="posts_imgs/")
    created_at = models.DateTimeField(auto_now_add=True)
    like_count = models.IntegerField(default=0)
    
    def __str__(self):
        return self.post_content[:10]
    
    
class Comments(models.Model):
    comment_content = models.CharField(max_length=200)
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)
    post = models.ForeignKey(Posts, on_delete=models.CASCADE)
    
    def __str__(self):
        return f"Added by {self.profile}"
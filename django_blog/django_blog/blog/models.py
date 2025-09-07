from django.db import models
from django.contrib.auth.models import User

class Post(models.Model):
    # Title of the blog post
    title = models.CharField(max_length=200)
    
    # Content body of the post
    content = models.TextField()
    
    # Auto-populated when the post is created
    published_date = models.DateTimeField(auto_now_add=True)
    
    # Link post to a user (author)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name="posts")

    def __str__(self):
        return self.title


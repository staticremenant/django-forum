from django.db import models
from django.contrib.auth.models import User
import PIL

# Create your models here.
class Post(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=200, blank=True)
    description = models.TextField(blank=True)
    image = models.ImageField(upload_to='images/%Y/%m/%d/', default=None, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title + '\n' + self.description

class Comment(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey('Post', on_delete=models.CASCADE)
    content = models.TextField(blank=True)
    image = models.ImageField(upload_to='images/%Y/%m/%d/', default=None, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.content

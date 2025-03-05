from django.db import models
from django.utils.text import slugify
from django.contrib.auth.models import User

class Post(models.Model):
    title = models.CharField(max_length=20)
    body = models.TextField()
    slug = models.SlugField(max_length=22, unique=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    status = models.CharField(choices=(("draft", "Draft"), ("published", "Published")), default="draft", max_length=10)
    published_date = models.DateTimeField(blank=True, null=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE,related_name="posted")
    class Meta:
        
        ordering = ("published_date","title")
    
    def __str__(self):
                 return self.title
    
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)

class Comment(models.Model):
    post = models.ForeignKey(Post, related_name='comments', on_delete=models.CASCADE)
    name = models.CharField(max_length=80)
    email = models.EmailField()
    body = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    active = models.BooleanField(default=True)

    class Meta:
        ordering = ('created',)

    def __str__(self):
        return f'Comment by {self.name} on {self.post}'


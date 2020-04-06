from django.db import models
from django.utils import timezone

class User(models.Model):
    email = models.CharField(max_length=100, default="") 
    password = models.CharField(max_length=100, default="") 
    username = models.CharField(max_length=100, default="") 
    is_admin = models.BooleanField(default=False)
    def __str__(self):
        return self.username

class Comment(models.Model):
    content = models.CharField(max_length=1000)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    pub_date = models.DateTimeField(default=timezone.now) 
    def __str__(self):
        return self.content

class Category(models.Model):
    name = models.CharField(max_length=200)
    def __str__(self):
        return self.name


class Blog(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=100, default="")
    description = models.CharField(max_length=2000, default="")
    category = models.ManyToManyField(Category, null=True)
    views = models.IntegerField(default=0)
    pub_date = models.DateTimeField(default=timezone.now)
    img_url = models.CharField(max_length=500, default="")
    comments = models.ManyToManyField(Comment, null=True)
    def __str__(self):
        return self.title



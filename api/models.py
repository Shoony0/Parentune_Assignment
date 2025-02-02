from django.db import models
from django.contrib.auth.models import User

class Child(models.Model):
    parent = models.ForeignKey(User, on_delete=models.CASCADE, related_name="children")
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    gender = models.CharField(max_length=10, choices=[('Male', 'Male'), ('Female', 'Female')])

class Blog(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    tags = models.JSONField(default=list)
    age_group = models.CharField(max_length=20)
    parent_interest = models.JSONField(default=list)
    views = models.IntegerField(default=0)

class UserActivity(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="activities")
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE)
    action = models.CharField(max_length=20, choices=[('like', 'Like'), ('share', 'Share'), ('read', 'Read')])
    timestamp = models.DateTimeField(auto_now_add=True)

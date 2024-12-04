# news/models.py
from django.db import models
from django.utils import timezone
from datetime import timedelta


class Article(models.Model):

    CATEGORY_CHOICES = [
        ('home','Home'),
        ('world', 'World'),
        ('politics', 'Politics'),
        ('sports', 'Sports'),
        ('entertainment', 'Entertainment'),
        ('innovations', 'Innovations'),
        ('bussiness', 'Bussiness'),
    ]

    title = models.CharField(max_length=200)
    content = models.TextField()
    image = models.ImageField(upload_to='article/images/', blank=True, null=True)
    video = models.FileField(upload_to='article/videos/', blank=True, null=True)
    published_date = models.DateTimeField(auto_now_add=True)
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES,default='home')
    like_count = models.IntegerField(default=0) 
    
    def __str__(self):
        return self.title

class Contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    contact_no = models.CharField(max_length=15)
    feedback = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} ({self.email})"


class Advertisement(models.Model):
    title = models.CharField(max_length=100, help_text="Title of the advertisement")
    image = models.ImageField(upload_to='advertisements/', blank=True, null=True, help_text="Upload an image for the ad")
    video_url = models.URLField(blank=True, null=True, help_text="Add a YouTube video URL")
    link = models.URLField(blank=True, null=True, help_text="Link to the advertisement's website")
    description = models.TextField(blank=True, null=True, help_text="Description or details about the ad")

    def __str__(self):
        return self.title
## a comment added ...
## a second command 
## a third command
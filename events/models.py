from django.db import models
from django.contrib.auth.models import User

# MODELS EVENTS
class Events(models.Model):
    # user        = models.ForeignKey(User, on_delete=models.CASCADE)
    event_image = models.ImageField(default='default.jpg',upload_to='images')
    event_type  = models.CharField(max_length=20)
    event_title = models.CharField(max_length=50)
    developer   = models.CharField(max_length=50)
    description = models.TextField()
    schedule    = models.CharField(max_length=50)
    location    = models.CharField(max_length=100)  



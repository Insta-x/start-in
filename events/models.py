from django.db import models
from authentication.models import User

# class Developer(models.Model): 
#    name = models.CharField(max_length=50)

# MODELS EVENTS
class Events(models.Model):
    user        = models.ForeignKey(User, on_delete=models.CASCADE, default=None, null=True, blank=True)
    # event_image = models.ImageField(default=None, null=True, blank=True, upload_to='event_images')
    event_type  = models.CharField(max_length=20)
    event_title = models.CharField(max_length=50)
    # developer   = models.ForeignKey(Developer, on_delete=models.CASCADE)
    description = models.TextField()
    schedule    = models.CharField(max_length=50)
    location    = models.CharField(max_length=100)
    # url_image   = models.TextField(default="/")  



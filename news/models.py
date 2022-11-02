from datetime import date
from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class NewsItems(models.Model):
    # user        = models.ForeignKey(User, on_delete=models.CASCADE)
    # news_image  = models.ImageField()
    date        = models.DateField()
    news_title  = models.CharField(max_length = 50)
    author      = models.CharField(max_length = 50)
    news_text   = models.TextField()    
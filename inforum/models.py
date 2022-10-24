from django.db import models
from django.contrib.auth import models as user_auth;
from django.utils import timezone;

# Create your models here.

class Forum(models.Model):
    user_id = models.ForeignKey(user_auth.User, on_delete=models.CASCADE);
    username= models.CharField(max_length=100);
    time_created = models.DateField(default=timezone.now());
    title = models.CharField(max_length=100);
    content = models.TextField(max_length=1000);


class Comment(models.Model):
    forum = models.ForeignKey("Forum", on_delete=models.CASCADE);
    from_user = models.ForeignKey(user_auth.User, on_delete=models.CASCADE);
    time_created = models.DateField(default=timezone.now());
    comment = models.TextField(max_length=250);

from django.db import models
from django.utils import timezone
from authentication.models import User

class Project(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    time_created = models.DateField(default=timezone.now)
    title = models.CharField(max_length=100)
    description = models.TextField(max_length=1000)
    donation_target = models.PositiveBigIntegerField()
    liked_by = models.ManyToManyField(User, related_name='projects_liked')

class Donation(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='donations')
    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name='donations')
    amount = models.PositiveBigIntegerField(default=1)
    date = models.DateField(default=timezone.now)
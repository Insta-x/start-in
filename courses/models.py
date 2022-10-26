from django.db import models

class Course(models.Model):
    course_name = models.CharField(max_length=200)
    course_creator = models.CharField(max_length=200)
    description = models.TextField()
    course_time = models.IntegerField()
    last_updated = models.DateTimeField(auto_now_add=True,blank=True)

# Create your models here.

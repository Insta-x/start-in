from django.db import models

class Course(models.Model):
    course_name = models.CharField(max_length=200)
    course_url = models.URLField(blank=False, null=False)
    thumbnail = models.ImageField(null=False, blank=True)
    
    def __str__(self):
        return self.course_name

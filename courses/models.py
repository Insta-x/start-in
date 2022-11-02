from django.db import models

class Course(models.Model):
    course_name = models.CharField(max_length=200)
    thumbnail = models.ImageField(null=False, blank =True)
    
    def __str__(self):
        return self.course_name

class Course_detail(models.Model):
    description = models.TextField()
    course_time = models.IntegerField()
    last_updated = models.DateTimeField(auto_now_add=True,blank=True)
    course_url = models.URLField(blank=False, null=False)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)

    def __str__(self):
        return self.course

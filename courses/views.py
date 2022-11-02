from django.shortcuts import render
from .models import Course, Course_detail

def show_courses(request):
    context = {'logged_in' : request.user.is_authenticated}
    return render(request, 'course.html', context)
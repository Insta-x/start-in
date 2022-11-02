from django.shortcuts import render
from .models import Course, Course_detail

def show_courses(request):
    context = {'logged_in' : request.user.is_authenticated}
    return render(request, 'courses.html', context)

def course(request):
    courses = Course.objects.all()
    context = {'courses': courses}
    return render(request,'courses.html', context)
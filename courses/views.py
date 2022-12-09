from django.shortcuts import render
from .models import Course
from django.core import serializers
from django.http import HttpResponse

def show_courses(request):
    context = {'logged_in' : request.user.is_authenticated}
    return render(request, 'courses.html', context)

def course(request):
    courses = Course.objects.all()
    context = {'courses': courses}
    return render(request,'courses.html', context)

def show_json_course(request):
    data_course = Course.objects.all()
    data = serializers.serialize('json', data_course)
    return HttpResponse(data, content_type='application/json')
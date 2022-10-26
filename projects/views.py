from turtle import title
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.shortcuts import render
from django.core import serializers
from requests import request
from .models import Project

def show_projects(request):
    context = {'logged_in' : request.user.is_authenticated}

    return render(request, 'show_projects.html', context)

def get_projects(request):
    data = Project.objects.filter(title__icontains=request.GET.get('search'))

    return HttpResponse(serializers.serialize('json', data), content_type='application/json')
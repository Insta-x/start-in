from turtle import title
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.shortcuts import render
from django.core import serializers
from django.db.models import Count
from requests import request
from .models import Project

def show_projects(request):
    context = {'logged_in' : request.user.is_authenticated}

    return render(request, 'show_projects.html', context)

def get_projects(request):
    data = Project.objects.filter(title__icontains=request.GET.get('search')).annotate(like_count=Count('liked_by')).order_by('-like_count')

    print(data)

    return HttpResponse(serializers.serialize('json', data), content_type='application/json')

def like_project(request):
    if request.user.is_authenticated:
        project_id = request.POST.get('id')
        project = Project.objects.get(pk=project_id)
        if request.user in project.liked_by.all():
            project.liked_by.remove(request.user)
        else:
            project.liked_by.add(request.user)
        return HttpResponse(serializers.serialize('json', [project, ]), content_type='application/json')

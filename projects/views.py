from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.shortcuts import render
from requests import request

def show_projects(request):
    context = {'logged_in' : request.user.is_authenticated}

    return render(request, 'show_projects.html', context)
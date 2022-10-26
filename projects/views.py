from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.shortcuts import render
from requests import request

def test(request):
    return HttpResponse('hello project')
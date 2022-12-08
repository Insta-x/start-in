from django.shortcuts import render

def index(request):
    return render(request, 'index.html', {"username" : request.user.username})
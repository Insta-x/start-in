from django.http import HttpResponse
from django.shortcuts import render
from django.core import serializers
import requests
import json

# Create your views here.
def show_news(request):
    r = requests.get('http://api.mediastack.com/v1/news?access_key=2c111a4cbf72fe3f061b178e19acc926&countries=us&categories=technology')
    res = r.json()
    data = res['data']
    title = []
    description = []
    image = []
    url = []
    for i in data:
        title.append(i['title'])
        description.append(i['description'])    
        image.append(i['image'])
        url.append(i['url'])
    newsItems = zip(title, description, image, url)
    context = {
        'newsItems': newsItems
    }
    return render(request, 'page.html', context)

def get_news_json(request):
    r = requests.get('http://api.mediastack.com/v1/news?access_key=2c111a4cbf72fe3f061b178e19acc926&countries=us&categories=technology')
    res = r.json()
    # print(r)
    # print(res)
    data = res['data']
    print(json.dumps(data))
    title = []
    description = []
    image = []
    url = []
    for i in data:
        title.append(i['title'])
        description.append(i['description'])    
        image.append(i['image'])
        url.append(i['url'])
    newsItems = zip(title, description, image, url)
    # print(newsItems)
    return HttpResponse(json.dumps(data), content_type="application/json")
from django.shortcuts import render
import requests

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
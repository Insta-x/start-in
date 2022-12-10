from django.urls import path
from news.views import show_news, get_news_json

app_name = 'news'

urlpatterns = [
    path('', show_news, name='news'),
    path('json/', get_news_json, name='get_news_json'),
]
from pydoc import Helper
from django.urls import path
from .views import *;

app_name = 'inforum'

urlpatterns = [
    path('', show_all_forum, name='show_all_forum'),
    path('get_all_forum/', get_all_forum, name='get_all_forum'),
]
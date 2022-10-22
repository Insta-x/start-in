from pydoc import Helper
from django.urls import path
from .views import *;

app_name = 'inforum'

urlpatterns = [
    path('', show_all_forum, name='show_all_forum')
]
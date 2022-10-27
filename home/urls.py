from pydoc import Helper
from xml.etree.ElementInclude import include
from django.urls import path
from .views import *;

app_name = 'home'

urlpatterns = [
    path('', index, name='index'),
]
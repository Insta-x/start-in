from pydoc import Helper
from xml.etree.ElementInclude import include
from django.urls import path
from home.views import hello_world

app_name = 'home'

urlpatterns = [
    path('', index, name='index'),
]
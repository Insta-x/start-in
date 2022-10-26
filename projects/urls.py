from pydoc import Helper
from django.urls import path
from .views import *

app_name = 'project'

urlpatterns = [
    path('', test, name='test')
]
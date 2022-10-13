from pydoc import Helper
from django.urls import path
from home.views import hello_world

app_name = 'home'

urlpatterns = [
    path('', hello_world, name='hello-world')
]
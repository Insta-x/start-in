from pydoc import Helper
from django.urls import path
from .views import show_projects

app_name = 'projects'

urlpatterns = [
    path('', show_projects, name='show_projects')
]
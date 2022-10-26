from pydoc import Helper
from django.urls import path
from .views import show_projects, get_projects

app_name = 'projects'

urlpatterns = [
    path('', show_projects, name='show_projects'),
    path('get-projects/', get_projects, name='get_projects')
]
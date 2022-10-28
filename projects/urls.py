from pydoc import Helper
from unicodedata import name
from django.urls import path
from .views import show_projects, get_projects, like_project, show_project

app_name = 'projects'

urlpatterns = [
    path('', show_projects, name='show_projects'),
    path('get-projects/', get_projects, name='get_projects'),
    path('like-project/', like_project, name='like_project'),
    path('project/<int:id>', show_project, name='show_project'),
]
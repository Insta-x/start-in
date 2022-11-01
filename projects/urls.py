from django.urls import path
from .views import show_projects, get_projects, get_user_projects, create_project, publish_project, like_project, show_project, donate_project, get_donations

app_name = 'projects'

urlpatterns = [
    path('', show_projects, name='show_projects'),
    path('get-projects/', get_projects, name='get_projects'),
    path('get-user-projects', get_user_projects, name='get_user_projects'),
    path('like-project/', like_project, name='like_project'),
    path('project/<int:id>', show_project, name='show_project'),
    path('publish/', publish_project, name='publish_project'),
    path('donate/', donate_project, name='donate_project'),
    path('get-donations/', get_donations, name='get_donations'),
    path('create-project/', create_project, name='create_project'),
]
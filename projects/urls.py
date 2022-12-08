from django.urls import path
from .views import show_projects, show_project, get_projects, get_user_projects, get_donations
from .views import create_project, edit_project, delete_project, publish_project, like_project, donate_project, done_project

app_name = 'projects'

urlpatterns = [
    path('', show_projects, name='show_projects'),
    path('get-projects/', get_projects, name='get_projects'),
    path('get-user-projects', get_user_projects, name='get_user_projects'),
    path('like-project/', like_project, name='like_project'),
    path('project/<int:id>', show_project, name='show_project'),
    path('edit/<int:id>', edit_project, name='edit_project'),
    path('delete/', delete_project, name='delete_project'),
    path('publish/', publish_project, name='publish_project'),
    path('done/', done_project, name='done_project'),
    path('donate/', donate_project, name='donate_project'),
    path('get-donations/', get_donations, name='get_donations'),
    path('create-project/', create_project, name='create_project'),
]
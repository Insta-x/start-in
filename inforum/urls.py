from pydoc import Helper
from django.urls import path
from .views import *;

app_name = 'inforum'

urlpatterns = [
    path('', show_all_forum, name='show_all_forum'),
    path('get_all_forum/', get_all_forum, name='get_all_forum'),
    path('add/', add_forum, name='add_forum'),
    path('add/json/', add_forum_json, name='add_forum_json'),
    path('delete_forum/<int:forum_id>', delete_forum, name='delete_forum'),
    path('get_all_forum/<str:category>', get_all_forum_by_category, name='get_all_forum_by_category'),
    path('get_forum/<int:forum_id>', get_forum, name='get_forum'),
    path('forum/<int:forum_id>', show_forum, name='show_forum'),
    path('forum/comment/<int:forum_id>', get_comment, name='get_comment'),
    path('forum/<int:forum_id>/comment/add', add_comment, name='add_comment'),
    path('forum/<int:forum_id>/comment/delete/<int:comment_id>', delete_comment, name='delete_comment'),
]
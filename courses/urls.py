from django.urls import path
from .views import show_courses, show_json_course

app_name = 'courses'

urlpatterns = [
    path('', show_courses, name='show_courses'),
    path('json', show_json_course, name="show_json"),
]
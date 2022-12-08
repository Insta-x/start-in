from django.urls import path
from .views import show_courses

app_name = 'courses'

urlpatterns = [
    path('', show_courses, name='show_courses'),
]
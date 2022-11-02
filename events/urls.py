from django.urls import path
from events.views import *

app_name = 'events'

urlpatterns = [
    path('', show_events, name='show_event'),
    # path('add/', add_events, name='add_events'),
    # path('json/', get_events_json, name='get_events_json'),
    # path('get-data-events/', get_data_events, name='get_data_events')
]
from django.urls import path
from events.views import *

app_name = 'events'

urlpatterns = [
    path('', show_events, name='show_event'),
    path('add/', add_events, name='add_events'),
    path('get_all_events/', get_all_events, name='get_all_events'),
    path('show_events_1/', show_events_1, name='show_events_1'),
    path('show_events_2/', show_events_2, name='show_events_2'),
    path('show_events_3/', show_events_3, name='show_events_3'),
    # path('json/', get_events_json, name='get_events_json'),
    # path('get-data-events/', get_data_events, name='get_data_events')
]
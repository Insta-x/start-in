from django.shortcuts import render
from events.models import Events

def show_events(request):
    data_events = Events.objects.all()

    context = {
        'list_events' : data_events
    }
    return render(request, "events.html", context)
from django import forms
from events.models import Events

class EventsForm(forms.ModelForm):

    event_image = forms.ImageField(required=True)
    event_type  = forms.CharField(max_length=20, required=True)
    event_title = forms.CharField(max_length=50, required=True)
    developer_name   = forms.CharField(max_length=50, required=True)
    description = forms.CharField(required=True)
    schedule    = forms.CharField(max_length=50, required=True)
    location    = forms.CharField(max_length=100, required=True)


    class Meta:
        model = Events
        fields = ('event_image', 'event_type', 'event_title', 'developer_name', 'description', 'schedule', 'location')
        
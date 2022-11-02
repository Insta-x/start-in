from django.shortcuts import render
from events.models import Events
from events.forms import EventsForm
import json
from django.http import JsonResponse, HttpResponse
from django.core import serializers

def show_events(request):
    data_events = Events.objects.all()

    context = {
        'list_events' : data_events
    }
    return render(request, "events.html", context)

def add_events(request):
    if request.method == "POST":
        bodyRequest = json.loads(request.body.decode("utf-8"))
        print(bodyRequest['url_image'])

        
        event_type = bodyRequest['event_type']
        event_title = bodyRequest['event_title']
        description = bodyRequest['description']
        schedule = bodyRequest['schedule']
        location = bodyRequest['location']
        url_image = bodyRequest['url_image']

        event = Events.objects.create(user=request.user, event_type=event_type, event_title=event_title, description=description, schedule=schedule, location=location, url_image=url_image)

        return JsonResponse({})
    else:
        return JsonResponse({})




# def add_events(request):
    
#     if request.method == 'POST':
#         print(request.method)
#         form = EventsForm(request.POST, request.FILES)

#         if form.is_valid():
#             print('is valid')
#             obj = form.save(commit=False)
#             developer_name = form.cleaned_data['developer_name']
#             print(developer_name)
#             # ngecek di database developer, ada yg namanya sesuai variabel developer gak,
#             # kalo ada, get object itu,
#             # kalo ngga, bikin objek Developer baru
#             developer_instance = Developer(name=developer_name)
#             developer_instance.save()
#             print('AAAAAAAAAAAAAAAAAAAAAAA')
#             print(developer_instance)
#             obj.developer = developer_instance
#             obj.save()

#             data = {
#                 "message":"SUBMIT BERHASIL"
#             }

#             json_object = json.dumps(data, indent=4)

#             return JsonResponse(json.loads(json_object))
#         else:
#             print('GAK VALID')
#             data = {
#                 "message":form.errors
#             }

#             json_object = json.dumps(data, indent=4)

#             return JsonResponse(json.loads(json_object))
#     else:
#         print('BUKAN POSTT')


#         context = {
#             'form': EventsForm()
#         }
#         return render(request, "add_events.html", context)


# def get_events_json(request):
#     data = Events.objects.all()

#     return HttpResponse(serializers.serialize('json',data))

# def get_data_events(request):
#     events = Events.objects.all()
#     data = []

#     for item in events:
#         item.url_image = item.event_image.url
#         data.append({'pk': item.pk, 'fields': {'user': item.user.username, 'event_type': item.event_type, 'event_title': item.event_title, 'description': item.description, 'schedule': item.schedule, 'location': item.location, 'url_image': item.url_image}}) 
#     data = {'data': data}
#     return JsonResponse(data)
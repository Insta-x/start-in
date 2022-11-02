from os import stat
import re
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.shortcuts import redirect, render
from django.core import serializers
from django.db.models import Count, Sum
from django.urls import reverse
from authentication.models import User
from django.contrib.auth.decorators import login_required
from .models import Project, Donation
from .forms import ProjectForm, DonationForm
import json

def show_projects(request):
    user_projects = Project.objects.filter(user=request.user) if request.user.is_authenticated else None

    context = {
        'logged_in' : request.user.is_authenticated,
        'user_projects' : True if user_projects else False,
    }

    return render(request, 'show_projects.html', context)

def show_project(request, id):
    project = Project.objects.get(pk=id)

    # print(Donation.objects.filter(project=id).aggregate(Sum('amount'))['amount__sum'])

    return render(request, 'show_project.html', {'project' : encode_project(project, request.user.id), 'logged_in' : request.user.is_authenticated})

@login_required(login_url='/auth/login/')
def create_project(request):
    if request.method == 'POST':
        form = ProjectForm(request.POST)
        if form.is_valid():
            new_task = form.save(commit=False)
            new_task.user = request.user
            new_task.save()
            form.save_m2m()
            return HttpResponseRedirect(reverse('projects:show_projects'))
    else:
        form = ProjectForm()
    return render(request, 'create_project.html', {'form': form})

def get_projects(request):
    data = Project.objects.filter(is_published=True).filter(title__icontains=request.GET.get('search')).annotate(like_count=Count('liked_by')).order_by('-like_count')

    return HttpResponse(json.dumps(encode_projects(data, request.user.id)), content_type='application/json')

def get_user_projects(request):
    data = Project.objects.filter(user=request.user).order_by('-time_created')

    return HttpResponse(json.dumps(encode_projects(data, request.user.id)), content_type='application/json')

def edit_project(request, id):
    project = Project.objects.get(pk=id)

    if not project:
        return HttpResponse(status=404)

    if project.is_published:
        return HttpResponse(status=403)

    if request.method == 'POST':
        project.title = request.POST.get('title')
        project.description = request.POST.get('description')
        project.donation_target = request.POST.get('donation_target')
        project.save()
        return redirect(reverse('projects:show_projects'))

    return render(request, 'edit_project.html', {'project' : project})

def delete_project(request):
    project = Project.objects.get(pk=request.POST.get('id'))

    if project.user != request.user:
        return HttpResponse(status=403)
    
    project.delete()
    return HttpResponse('Success', content_type='text/plain')

def publish_project(request):
    project = Project.objects.get(pk=request.POST.get('id'))

    if project.user != request.user:
        return HttpResponse(status=403)
    
    project.is_published = True
    project.save()
    return HttpResponse(json.dumps([encode_project(project, request.user.id), ]), content_type='application/json')


@login_required(login_url='/auth/login/')
def like_project(request):
    if request.user.is_authenticated:
        project_id = request.POST.get('id')
        project = Project.objects.get(pk=project_id)
        if project.is_published:
            if request.user in project.liked_by.all():
                project.liked_by.remove(request.user)
            else:
                project.liked_by.add(request.user)
        return HttpResponse(json.dumps([encode_project(project, request.user.id), ]), content_type='application/json')

def donate_project(request):
    if not request.user.is_authenticated:
        return HttpResponse(status=403)

    if request.method != 'POST':
        return HttpResponse(status=403)
    
    form = DonationForm(request.POST)
    if form.is_valid():
        new_donation = form.save(commit=False)
        new_donation.user = request.user
        new_donation.save()
        form.save_m2m()
        return HttpResponse(serializers.serialize('json', [new_donation, ]), content_type='application/json')

def get_donations(request):
    donations = Donation.objects.filter(project=request.GET.get('project_id'))
    # print(request.GET.get('project_id'))
    donation_sum = donations.aggregate(Sum('amount'))['amount__sum'] or 0
    donators = []

    for donation in donations.order_by('-amount')[:50]:
        donators.append({'username' : User.objects.get(pk=donation.user_id).username, 'amount' : donation.amount})
    
    # print(donations, donation_sum, donators)

    return HttpResponse(json.dumps({'donation_sum' : donation_sum, 'donators' : donators}), content_type='application/json')

def done_project(request):
    project = Project.objects.get(pk=request.POST.get('id'))

    if project.user != request.user:
        return HttpResponse(status=403)
    
    project.is_done = True
    project.save()
    return HttpResponse(json.dumps([encode_project(project, request.user.id), ]), content_type='application/json')

def encode_projects(data_query_set, user_id):
    data_list = []
    for e in data_query_set:
        data_list.append(encode_project(e, user_id))
    return data_list

def encode_project(project, user_id):
    dict_data = json.loads(serializers.serialize('json', [project, ])[1:-1])
    dict_data['fields']['current_donation'] = Donation.objects.filter(project=project.pk).aggregate(Sum('amount'))['amount__sum'] or 0
    dict_data['fields']['owner_username'] = User.objects.get(pk=dict_data['fields']['user']).username
    dict_data['fields']['like_count'] = len(dict_data['fields']['liked_by'])
    dict_data['fields']['is_liked'] = user_id in dict_data['fields']['liked_by']
    del dict_data['fields']['liked_by']
    return dict_data
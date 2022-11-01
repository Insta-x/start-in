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
        'user_projects' : encode_projects(user_projects, request.user),
    }

    return render(request, 'show_projects.html', context)

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
    data = Project.objects.filter(title__icontains=request.GET.get('search')).annotate(like_count=Count('liked_by')).order_by('-like_count')

    return HttpResponse(json.dumps(encode_projects(data, request.user.id)), content_type='application/json')

@login_required(login_url='/auth/login/')
def like_project(request):
    if request.user.is_authenticated:
        project_id = request.POST.get('id')
        project = Project.objects.get(pk=project_id)
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

def show_project(request, id):
    project = Project.objects.get(pk=id)

    # print(Donation.objects.filter(project=id).aggregate(Sum('amount'))['amount__sum'])

    return render(request, 'show_project.html', {'project' : encode_project(project, request.user.id), 'logged_in' : request.user.is_authenticated})

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
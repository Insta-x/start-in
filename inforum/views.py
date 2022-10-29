from unicodedata import category
from django.contrib.auth import logout
from django.shortcuts import render;
from .models import *;
from django.http import HttpResponse, HttpResponseRedirect;
from django.core import serializers;
from django.shortcuts import redirect;
from django.contrib import messages;
from django.contrib.auth import authenticate, login, models;
from django.contrib.auth.decorators import login_required;
from django.urls import reverse;
from authentication.models import NormalUserProfile;
import datetime;
import json;

# Create your views here.

def show_all_forum(request):
    context = {
        'user_id' : request.user.id,
        'username' : request.user.username,
        'user_type' : request.user.type if request.user.id != None else "",
    }

    return render(request, 'inforum.html', context) 

def get_all_forum(request):
    forums = Forum.objects.all();
    return HttpResponse(serializers.serialize("json", forums ), content_type="application/json")

def get_all_forum_by_category(request, category):
    forums = Forum.objects.filter(category=category.lower());
    return HttpResponse(serializers.serialize("json", forums ), content_type="application/json")


def show_forum(request, forum_id):
    forum = Forum.objects.get(id=forum_id);
    print(forum)
    related_forums = Forum.objects.filter(category=forum.category);
    if len(related_forums) > 5:
        related_forums= related_forums[0:5]
    print(related_forums)
    
    return render(request, "forum-page.html", {"forum_id" : forum_id, "user" : request.user, "user_type" : request.user.type if request.user.id != None else "", "related_forums": related_forums, "forum_title": Forum.objects.get(id=forum_id).title}) 
    
def get_forum(request, forum_id):
    forum = Forum.objects.filter(id=forum_id);
    
    #TODO:return data and render template html
    return HttpResponse(serializers.serialize("json", forum), content_type="application/json")

@login_required(login_url="/auth/login")
def add_forum(request):
    if request.method == "POST":

        #TODO: validate request payload
        newForum = Forum(user_id=request.user, username=request.user.username);
        newForum.title = request.POST.get("title");
        newForum.content = request.POST.get("content");
        newForum.category= request.POST.get("category");
        newForum.save();
        return HttpResponse(serializers.serialize("json", [newForum]), content_type="application/json")

    return HttpResponse("only POST method allowd!")

@login_required(login_url="/auth/login")
def add_comment(request, forum_id):
    if request.method == "POST":

        #TODO: validate request payload
        user = NormalUserProfile.objects.get(user=request.user);
        newComment = Comment(from_user=request.user, username=user.name, user_job = user.job );
        newComment.forum = Forum.objects.get(id=forum_id);
        newComment.comment = request.POST.get("comment");
        newComment.save();
        return HttpResponse(serializers.serialize("json", [newComment]), content_type="application/json")

    return HttpResponse("only POST method allowd!")

@login_required(login_url="/auth/login")
def get_comment(request, forum_id):
    if request.method == "GET":
        forum = Forum.objects.filter(id=forum_id).first()
        comments = Comment.objects.filter(forum=forum)

        return HttpResponse(serializers.serialize("json", comments), content_type="application/json")

@login_required(login_url="/auth/login")
def delete_comment(request,forum_id, comment_id):
    if request.method == "DELETE":

        #TODO: validate request payload
        forum = Forum.objects.get(id=forum_id);
        queryComment = Comment.objects.get(from_user=request.user, forum=forum,id=comment_id)
        queryComment.delete();
        return HttpResponse("successfully deleted your comment")

    return HttpResponse("only DELETE method allowd!")

@login_required(login_url="/auth/login")
def delete_forum(request,forum_id):
    if request.method == "DELETE":

        #TODO: validate request payload
        forum = Forum.objects.filter(id=forum_id).first();
        print(forum)
        if(forum):
            forum.delete();
        return HttpResponse("successfully deleted your forum")

    return HttpResponse("only DELETE method allowd!")
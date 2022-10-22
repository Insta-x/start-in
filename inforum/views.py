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
import datetime;
import json;

# Create your views here.

def show_all_forum(request):

    return render(request, 'inforum.html') 

def get_all_forum(request):
    forums = Forum.objects.all();
    return HttpResponse(serializers.serialize("json", forums ), content_type="application/json")


def show_forum(request):
    
    #TODO:render forum.html

    return 
    
def get_forum(request, id):
    forum = Forum.objects.filter(id=id);
    comments = Comment.objects.filter(forum=forum);
    context = {'forum' : forum, 'comments' : comment}
    
    #TODO:return data and render template html
    return HttpResponse(serializers.serialize("json", context ), content_type="application/json")

@login_required(login_url="/")
def add_forum(request):
    if request.method == "POST":

        #TODO: validate request payload
        newForum = Forum(creator=request.user);
        newForum.title = request.POST.get("title");
        newForum.content = request.POST.get("content");
        newForum.save();
        return HttpResponse("succesfully created your forum!")

    return HttpResponse("only POST method allowd!")

@login_required(login_url="/")
def add_comment(request, forum_id):
    if request.method == "POST":

        #TODO: validate request payload
        newForum = Forum(from_user=request.user);
        newForum.forum = Forum.objects.filter(id=forum_id);
        newForum.comment = request.POST.get("comment");
        newForum.save();
        return HttpResponse("comment has been added!")

    return HttpResponse("only POST method allowd!")

@login_required(login_url="/")
def delete_comment(request,forum_id, comment_id):
    if request.method == "DELETE":

        #TODO: validate request payload
        forum = Forum.objects.filter(id=forum_id);
        queryComment = Comment.objects.filter(from_user=request.user, forum=forum,id=comment_id)
        queryComment.delete();
        return HttpResponse("successfully deleted your comment")

    return HttpResponse("only DELETE method allowd!")

@login_required(login_url="/")
def delete_forum(request,forum_id):
    if request.method == "DELETE":

        #TODO: validate request payload
        forum = Forum.objects.filter(id=forum_id);
        if(forum.creator == request.user):
            forum.delete();
        return HttpResponse("successfully deleted your forum")

    return HttpResponse("only DELETE method allowd!")
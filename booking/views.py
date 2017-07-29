# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib.auth.decorators import login_required
from django.shortcuts import render,get_object_or_404,render_to_response
from django.http import HttpResponseRedirect
from .forms import BookForm
from .models import Book
from .models import profile
from django.contrib import messages
from .forms import  profileForm


def index(request):
    context = {}
    return render(request,"index.html",context)


def about(request):
    context = {}
    return render(request,"about.html",context)



@login_required
def userProfile(request,user=None):
    user = request.user
    instance = get_object_or_404(profile, user=request.user)
    context = {
        'user': user,
      "instance": instance,  #detail
    }

    return render(request,"profile.html",context)




#todo make sure the updateprofile url redirects back to the profile page

@login_required
def update_profile(request,user=None):
    #profile = profile.object.get(user=request.user)
    instance = get_object_or_404(profile,user=request.user)
    form = profileForm(request.POST or None,request.FILES or None,instance=instance)
    #form = profileForm(initial={'description':profile.description})
    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()
        messages.success(request, "Successfully Updated Your Profile")
        return HttpResponseRedirect(instance.get_absolute_url())
    context = {
        "form":form,
        "instance":instance,
    }
    return  render(request,"update_profile.html",context)




@login_required
def book_ticket(request): #post_create
    form = BookForm(request.POST or None)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.user = request.user
        instance.save()
        messages.success(request,"Successfully Booked")
        return HttpResponseRedirect(instance.get_absolute_url())
    else:
        messages.error(request,"Not Booked!!")
    context = {
        "form":form,
    }
    return render(request,"book_form.html",context)


@login_required
def ticket_update(request,id=None): #post_update
    instance = get_object_or_404(Book, id=id)
    form = BookForm(request.POST or None,instance=instance)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()
        messages.success(request, "Successfully Updated Your Ticket")
        return HttpResponseRedirect(instance.get_absolute_url())
    context = {
        "instance": instance,
        "form": form,
    }
    return render(request,"book_form.html",context)



@login_required
def ticket_detail(request, id=None): #post_detail
    instance = get_object_or_404(Book,id=id)
    context = {
        "instance":instance,
    }
    return render(request,"ticket_detail.html",context)

@login_required
def booking_history(request): #Post_list
    user = request.user
    queryset= Book.objects.all()
    context = {
        "ticket_list":queryset,
        "title":"Booking History" , # list
        "user": user
    }
    return render(request,"profile.html",context)

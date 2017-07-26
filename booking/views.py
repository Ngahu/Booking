# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib.auth.decorators import login_required
from django.shortcuts import render
# Create your views here.


def index(request):
    context = {}
    return render(request,"index.html",context)


def about(request):
    context = {}
    return render(request,"about.html",context)



@login_required
def userProfile(request):
    user = request.user
    context = {'user':user}

    return render(request,"profile.html",context)


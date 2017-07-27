# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.contrib.auth.decorators import login_required



@login_required
def checkout(request):
    if request.method == 'POST':
        print request.POST
    context = {}
    return render(request,"checkout.html",context)



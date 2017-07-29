# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import Book,userStripe,profile


class bookAdmin(admin.ModelAdmin):
    class Meta:
        model = Book

admin.site.register(Book,bookAdmin)
# Register your models here.

class userStripeAdmin(admin.ModelAdmin):
    class Meta:
        model = userStripe

admin.site.register(userStripe,userStripeAdmin)


class profile_pic(admin.ModelAdmin):
    class Meta:
        model = profile

admin.site.register(profile,profile_pic)

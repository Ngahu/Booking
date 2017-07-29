# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.core.urlresolvers import reverse
from django.db import models
from django.conf import settings
# Create your models here.
from allauth.account.signals import user_logged_in,user_signed_up
import stripe

stripe.api_key = settings.STRIPE_SECRET_KEY


class Book(models. Model):
    ONEWAY = 'ONE'
    TWOWAY = 'TWO'
    #the kids section
    AGE_BTN = 'age_1'
    AGE_ABV = 'age_2'
    AGE_NONE= 'no kid'
    #Prefered class
    FIRST_CLASS = 'Business'
    ECONOMY = 'Economy'

    where_from = models.CharField(max_length=50)
    where_to = models.CharField(max_length=50)
    date_travelling = models.DateField(auto_now=False,auto_now_add=False)
    class_of_choice = (
        (FIRST_CLASS,'Business'),
        (ECONOMY,'Economy')
    )
    class_of_choice = models.CharField(max_length=30, choices= class_of_choice,null=False,default=ECONOMY)
    travelling_persons = models.IntegerField(default=1)
    kids_accompany_choices = (
        (AGE_BTN,'Age btwn 3-11 years'),
        (AGE_ABV,'Age above 11 years'),
        (AGE_NONE,'No kid')
    )
    kids = models.CharField(max_length=10,choices=kids_accompany_choices,null=False)

    def __unicode__(self):
        return self.where_from

    def get_absolute_url(self):
        return reverse("booking:detail",kwargs={"id":self.id})


def upload_location(instance,filename):
    return "%s/%s" %(instance.user,filename)


class profile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, null=True, blank=True)
    description = models.TextField(null=True,blank=True)
    profile_picture = models.ImageField(null=True,
                                        upload_to=upload_location,
                                        blank=True,
                                        )

    def __unicode__(self):
        return self.user.username
    def get_absolute_url(self):
        return reverse("booking:userProfile",kwargs={"user":self.user})


class userStripe(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL)
    stripe_id = models.CharField(max_length=200, null=True,blank=True)

    def __unicode__(self):
        if self.stripe_id:
            return str(self.stripe_id)
        else:
            return self.user.username



def stripeCallback(sender,request,user,**kwargs):
    user_stripe_account, created = userStripe.objects.get_or_create(user=user)
    if created:
        print 'created for %s'%(user.username)
    if user_stripe_account.stripe_id is None or user_stripe_account.stripe_id == '':
        new_stripe_id  = stripe.Customer.create(email=user.email)
        user_stripe_account.stripe_id = new_stripe_id['id']
        user_stripe_account.save()



def profileCallback(sender,request,user,**kwargs):
    userProfile,is_created = profile.objects.get_or_create(user=user)
    if is_created:
        userProfile.name = user.username
        userProfile.save()

user_logged_in.connect(stripeCallback)
user_signed_up.connect(profileCallback)
user_signed_up.connect(stripeCallback)

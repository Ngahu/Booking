# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Book(models. Model):
    ONEWAY = 'ONE'
    TWOWAY = 'TWO'
    #the kids section
    AGE_BTN = 'age_1'
    AGE_ABV = 'age_2'
    #Prefered class
    FIRST_CLASS = 'Business'
    ECONOMY = 'Economy'
    where_from = models.CharField(max_length=50)
    where_to = models.CharField(max_length=50)
    date_leaving = models.CharField(max_length=20)
    type_of_ticket_choices = (
        (ONEWAY,'Oneway'),
        (TWOWAY,'Twoway'),
    )
    type_of_ticket = models.CharField(max_length=3,choices=type_of_ticket_choices,default=ONEWAY)
    class_of_choice = (
        (FIRST_CLASS,'Business'),
        (ECONOMY,'Economy')
    )
    class_of_choice = models.CharField(max_length=30, choices= class_of_choice,null=False,default=ECONOMY)
    travelling_persons = models.IntegerField(default=1)
    kids_accompany_choices = (
        (AGE_BTN,'Age btwn 3-11 years'),
        (AGE_ABV,'Age above 11 years'),
    )
    kids = models.CharField(max_length=10,choices=kids_accompany_choices,null=True)

    def __unicode__(self):
        return self.where_from

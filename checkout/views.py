# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.conf import settings
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
import stripe


stripe.api_key = settings.STRIPE_SECRET_KEY



@login_required
def check_out(request):
    publishKey = settings.STRIPE_PUBLISHABLE_KEY
    customer_id = request.user.userstripe.stripe_id
    if request.method == 'POST':
        token  = request.POST['stripeToken']
        # Charge the user's card:
        customer = stripe.Customer.retrieve(customer_id)
        customer.sources.create(source=token)
        charge = stripe.Charge.create(
            amount=1000, #amount in cents
            currency="usd",
            description="Example charge",
            customer = customer
        )
    context = {
        "publishKey": publishKey
    }
    return render(request,"checkout.html",context)




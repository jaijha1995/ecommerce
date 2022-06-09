from django.shortcuts import render , redirect

from django.contrib.auth.hashers import  check_password
from store.models.customer import Customer
from django.views import  View
from store.models.product import  offer


class offer(View):
    def get(self , request):
        offer = list(request.session.get('offer').keys())
        offer = offer.get_offer_by_id(offer)
        print(offer)
        return render(request , 'offer.html' , {'offer' : offer} )

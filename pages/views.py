from django.shortcuts import render
from django.http import HttpResponse
from listings.models import Listing
from realtors.models import Realtor
from listings.choices import price_choices,bedroom_choices,state_choices

# Create your views here.

def index(request):
    listingsHome = Listing.objects.order_by('-list_date').filter(is_published=True)[:3] # [:3] means only showing 3 listings
    context = {
        'listings': listingsHome,
        'state_choices': state_choices,
        'bedroom_choices': bedroom_choices,
        'price_choices':price_choices,
    }
    return render(request,'pages/index.html', context)


def about(request):

    # Get all realtors
    realtorsAll = Realtor.objects.order_by('-hire_date')

    # Get mvp
    mvpRealtors = Realtor.objects.all().filter(is_mvp=True)

    context = {
        'realtors': realtorsAll,
        'mvpRealtors': mvpRealtors,
    }
    return render(request,'pages/about.html',context)

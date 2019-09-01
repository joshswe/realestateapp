from django.shortcuts import render, get_object_or_404
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from .models import Listing
from .choices import price_choices,bedroom_choices,state_choices


# Create your views here.
def index(request):

    listingsAll = Listing.objects.order_by('-list_date').filter(is_published=True) #Most recent listings should be first and only those published will be shown

    paginator = Paginator(listingsAll, 3)

    page = request.GET.get('page') #'page' is the URL parameter that we are looking for
    paged_listingsAll = paginator.get_page(page)

    context = {
        'listings': paged_listingsAll
    }

    return render(request, 'listings/listings.html',context)

def listing(request, listing_id):

    listing = get_object_or_404(Listing, pk=listing_id)  # If it doesn't exist it will return 404
    context = {
        'listing': listing
    }
    return render(request, 'listings/listing.html',context)

def search(request):

    queryset_list = Listing.objects.order_by('-list_date')

    # Keywords in the search form
    if 'keywords' in request.GET:
        keywords = request.GET['keywords'] #'keywords' is the form field
        if keywords:
            queryset_list = queryset_list.filter(description__icontains=keywords)

    # City
    if 'city' in request.GET:
        city = request.GET['city']
        if city:
            queryset_list = queryset_list.filter(city__iexact=city)

    # State
    if 'state' in request.GET:
        state = request.GET['state']
        if state:
            queryset_list = queryset_list.filter(state__iexact=state)

    # Bedrooms
    if 'bedrooms' in request.GET:
        bedrooms = request.GET['bedrooms']
        if bedrooms:
            queryset_list = queryset_list.filter(bedrooms__iexact=bedrooms) # 'lte' can be used for "less than and equal to"

    # Price
    if 'price' in request.GET:
        price = request.GET['price']
        if price:
            queryset_list = queryset_list.filter(price__lte=price) # 'lte' can be used for "less than and equal to"

    context = {
        'state_choices': state_choices,
        'bedroom_choices': bedroom_choices,
        'price_choices':price_choices,
        'listings': queryset_list,
        'values': request.GET
    }
    return render(request, 'listings/search.html',context)
from django.shortcuts import render
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from .models import Listing


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
    return render(request, 'listings/listing.html')

def search(request):
    return render(request, 'listings/search.html')
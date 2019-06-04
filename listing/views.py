from django.shortcuts import render
from .forms import NewListing

# Create your views here.
    
def create_listing(request):
    """Return the listing.html file
    Used for each individual listing once clicked in dashboard"""
    
    new_listing_form = NewListing(request.POST)
    return render(request, 'listing.html', {"new_listing": new_listing_form})

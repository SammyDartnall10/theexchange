from django.shortcuts import render, get_object_or_404, redirect
from .forms import NewListing
from .models import Listing

# Create your views here.
    

def all_listings(request):
    "Get all instances of listings"
    listings = Listing.objects.all()
    return render(request, "listing.html", {"listings": listings})
    
def create_listing(request, pk=None):
    """Create a post """
    listing = get_object_or_404(Listing, pk= pk) if pk else None
    if request.method == "POST":
        form = NewListing(request.POST, request.FILES, instance=listing)
        if form.is_valid():
            listing = form.save()
            return redirect(listing, listing.pk)
    else:
        form= NewListing(instance=listing)
    return render(request, 'listing.html', {'form': form})

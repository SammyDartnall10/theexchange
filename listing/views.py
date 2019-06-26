from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponseForbidden, HttpResponse
from .forms import NewListing, NewListingArchive
from .models import Listing

# Create your views here.

def create_listing_archive(request):
    print(request.user)
    if not request.user.is_authenticated:
        return redirect('login')
    else:
        if request.method == "POST":
            form = NewListing(request.POST, request.FILES)
            if form.is_valid():
                listing = form.save(commit=False)
                listing.owner = request.user
                listing.save()
                return redirect('profile')
        else:
            form = NewListing()


    return render(request, 'createnew.html', {'form': form})
    
def get_listings(request):
    """
    Create a view that will return a list
    of Posts that were published prior to 'now'
    and render them to the 'blogposts.html' template
    """
    listings = Listing.objects.all()
    return render(request, "exchange.html", {'listings': listings})
    
def create_listing(request):
    if request.method == 'POST':
        form = NewListing(request.POST, request.FILES)
        if form.is_valid():
            listing = form.save(commit=False)
            listing.user = request.user  # The logged-in user - re-fill in this field automatically
            listing.save()
            return redirect('/')
    else:
        form = NewListing()
    return render(request, 'createnew.html', {'form': form})
    
    
"""
def create_listing(request, pk=None):
    #Create a post - looks to see if theres an existing post
    listing = get_object_or_404(Listing, pk= pk) if pk else None
    if request.method == "POST":
        form = NewListing(request.POST, request.FILES, instance=listing)
        if form.is_valid():
            listing = form.save()
            return redirect(listing, listing.pk)
    else:
        form= NewListing(instance=listing)
    return render(request, 'createnew.html', {'form': form})
""" 
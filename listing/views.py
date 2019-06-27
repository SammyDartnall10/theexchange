from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponseForbidden, HttpResponse
from .forms import NewListing, NewListingArchive
from .models import Listing

# Create your views here.
    
def get_listings(request):
    """
    pulls in all lisitings in one query set
    """
    listings = Listing.objects.all()
    return render(request, "exchange.html", {'listings': listings})
    
def create_listing(request):
    if request.method == 'POST':
        form = NewListing(request.POST, request.FILES)
        if form.is_valid():
            listing = form.save(commit=False)
            listing.created_by = request.user  # The logged-in user - re-fill in this field automatically
            listing.save()
            return redirect('profile')
    else:
        form = NewListing()
    return render(request, 'createnew.html', {'form': form})
    
def edit_listing(request, pk):
    
    listing = get_object_or_404(Listing, pk=pk)
    if request.user.is_authenticated and request.user == listing.created_by or request.user.is_superuser: 
        if request.method == "POST":
            form = NewListing(request.POST, request.FILES, instance=listing)
            if form.is_valid():
                listing = form.save()
                return redirect('detail.html')        
        else:
            form = NewListing(instance=listing)
    else: 
        return HttpResponseForbidden()
        
    return render(request, 'createnew.html', {'form': form})
    #rendering the createnew file as its the same- wil display the info already saved and then save over with the edits. Linked in URLs
    
def listing_detail(request, pk):
    """
    Create a view that returns a single
    Post object based on the post ID (pk) and
    render it to the 'postdetail.html' template.
    Or return a 404 error if the post is
    not found
    """
    listing = get_object_or_404(Listing, pk=pk)
    return render(request, "listing_detail.html", {'listing': listing})   
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
from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponseForbidden, HttpResponse
from .forms import NewListing, NewListingArchive, UploadUpvotes
from django.contrib.auth.models import User
from .models import Listing, Upvotes

# Create your views here.
    
def filtered_listings(request):
    """
    search based on text input - returns listings
    """
    if request.method =="POST":
        search_criteria = request.POST.get('search-listings')
        print(search_criteria)
        listings = Listing.objects.filter(tag__contains=search_criteria)
        print(listings)
        return render(request, "filtered_results.html", {'listings': listings})
    else:
        return HttpResponse("Sorry, we appear to be having a slight issue at the moment - please try again")
        

    
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
                return redirect('profile')        
        else:
            form = NewListing(instance=listing)
    else: 
        return HttpResponseForbidden()
        
    return render(request, 'edit_listing.html', {'form': form})
    #rendering the createnew file as its the same- wil display the info already saved and then save over with the edits. Linked in URLs
    
def listing_detail(request, pk):
    """
    Create a view that returns a single Post object based on the post ID (pk) and render it to the 'postdetail.html' template.
    Or return a 404 error if the post is not found
    """
    listing = get_object_or_404(Listing, pk=pk)
    return render(request, "listing_detail.html", {'listing': listing})  

def view_listing(request, pk):
    """
    Create a view that returns a single Post object based on the post ID (pk) and render it to the 'postdetail.html' template.
    Or return a 404 error if the post is not found
    """
    listing = get_object_or_404(Listing, pk=pk)
    return render(request, "view_listing.html", {'listing': listing})    
    
def testcall(request, pk):
    """Take the pk from the ajax call and use to find listing id. Add a new upvote entry in the upvote table with the current user as the upviter to record who voted for what"""
    listing = get_object_or_404(Listing, pk=pk)
    voter = request.user
    if request.method == "POST":
            form = UploadUpvotes(request.POST, request.FILES)
            if form.is_valid():
                upvote = form.save(commit=False)
                upvote.voter = voter  
                upvote.listing_upvoted = listing
                listing.save()
                return redirect('/')
            else:
                return HttpResponse("Well, we got past the is request.method == POST bit.. but that form didnt work.. ")
    else: 
        return HttpResponse("the request method wasnt POST ")
    
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
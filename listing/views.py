from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponseForbidden, HttpResponse
from .forms import NewListing, NewListingArchive, UploadUpvotes
from django.contrib.auth.models import User
from .models import Listing, Upvotes
from django.views.decorators.csrf import csrf_exempt

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
    #
    #1. Retrieve list of upvotes for logged in user
    #2. Instead of using a list of objects, change it to just be a list of the listing names within the list of upvotes - #`upvoting_listing_names = [upvote.listing_updated.title for upvote in upvotes]`
    #3. Return the list of upvotes with the listings - `{'listings': listings, 'upvoting_listing_names': upvoting_listing_names}`
    #4. In the template, when iterating over the listings, put an if statement around the heart icon and if `listing.title` is in the #list ofupvotes, make the heart orange - `{% if listing.title in upvoting_listing_names %} display orange heart {% else %} #display black heart {% endif %}`
    #swap titile for pk 
#---------------------------------------------
    #longhabd version - use listi comprehesions - 
    user = request.user
    upvoted = Upvotes.objects.filter(voter = user).values_list('listing_upvoted', flat=True)
   
    
    print(upvoted)
    print(type(upvoted))
    print("hello")

    #for upvote in upvotes:
    #    upvoting_listing_names.append(upvote.listing_upvoted.title)
    listings = Listing.objects.all()
    
    return render(request, "exchange.html", {'listings': listings, 'upvoted': upvoted})

    
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
    
@csrf_exempt
def upvote(request):
    """Take the pk from the ajax call and use to find listing id. Add a new upvote entry in the upvote table with the current user as the upviter to record who voted for what"""
    print("got to the upvote view")
    pk = request.POST['pk']
    listing = get_object_or_404(Listing, pk=pk)
    voter = request.user

    upvote_instance = Upvotes.objects.create(voter=voter, listing_upvoted=listing)
    
    return redirect(request, 'exchange.html')
    
    #TODO - create new record in upvote table 
    #return JSON respone that says 200 successssful - can feed back to user 

@csrf_exempt
def downvote(request):
    """Take the pk from the ajax call and use to find listing id. Add a new upvote entry in the upvote table with the current user as the upviter to record who voted for what"""
    
    pk = request.POST['pk']
    listing = get_object_or_404(Listing, pk=pk)
    voter = request.user
    
    downvote_instance = Upvotes.objects.delete(voter=voter, listing_upvoted=listing)
    
    
    return render(request, 'exchange.html')
    
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
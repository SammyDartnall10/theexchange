from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponseForbidden, HttpResponse
from .forms import NewListing, UploadUpvotes
from django.contrib.auth.models import User
from .models import Listing, Upvotes
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required
from django.db.models import Count, F
from django.contrib import auth, messages


# Create your views here.
    
def filtered_listings(request):
    """
    search based on text input - returns listings, or an error message if no matching criteria. 
    """
    if request.method =="POST":
        search_criteria = request.POST.get('search-listings')
        print(search_criteria)
        listings = Listing.objects.filter(content__icontains=search_criteria)
        if listings:
            print(listings)
            return render(request, "filtered_results.html", {'listings': listings})
        else :
            messages.success(request, "Sorry, no matching results! Please try again")
            return render(request, "filtered_results.html", {'listings': listings})
    
    else:
        return render(request, "error.html")
        

@login_required    
def get_listings(request):
    """
    pulls in all lisitings in one query set. Ordering is done on count - this is separate to the upvotes property. Need to keep the two separate as trying to order by the upvotes property results in duplicate records being shown. Fix in progress (#TODO for later)
    the really annoying thing about this is the upvotes type when print (type(listing.upvotes)) in a for loop to unpack the query set returns type <class 'int'> - and returns one number/int for each listing. But then when you render it in the template it makes duplicates. 
    """
   
    user = request.user
    upvoted = Upvotes.objects.filter(voter = user).values_list('listing_upvoted', flat=True) #list of all the things the current user has liked - is used to set black or red color on heart icon in html template and also on-click event. 
    listings = Listing.objects.all().order_by('-count')
    for listing in listings:
        print (listing.upvotes)
        print (type(listing.upvotes))
    
    return render(request, "exchange.html", {'listings': listings, 'upvoted': upvoted})

    
def create_listing(request):
    """
    Fairly straightforward - takes a form based on a model and makes a new listing based on that model. The user feild is hidden to stop users intentionally or unintentionally adding listings under the wrong name. 
    """
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
    """
    Can edit the details that are displayed in the exchange, not hidden fields such as id, or created by. This way the right listings will stay with the right users. 
    """
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
        
    return render(request, 'edit_listing.html', {'listing': listing, 'form': form})
    #rendering the createnew file as its the same- wil display the info already saved and then save over with the edits. Linked in URLs
    

def listing_detail(request, pk):
    """
    Create a view that returns a single Listing object based on the ID (pk) and render it to the template. User can then click edit details. 
    """
    listing = get_object_or_404(Listing, pk=pk)
    return render(request, "listing_detail.html", {'listing': listing})  

def view_listing(request, pk):
    """
    A read only view - not editable 
    """
    listing = get_object_or_404(Listing, pk=pk)
    return render(request, "view_listing.html", {'listing': listing})  
    
def delete_listing(request, pk):
    """
    Deleting instance of Listing - Modal is in HTML to stop accidental deleting 
    """
    listing = get_object_or_404(Listing, pk=pk)
    delete_instance = Listing.objects.filter(id=listing.id).delete()
    messages.success(request, "Listing Deleted")
    return redirect('profile')
    
@csrf_exempt
def upvote(request):
    """Take the pk from the ajax call and use to find listing id. Add a new upvote entry in the upvote table with the current user as the upvoter to record who voted for what. At the same time increase the count vote by one - the upvotes feild and count field should match. Count is whay is used to order the listings to prevent duplicate records being rendered in the exchange.html """
    pk = request.POST['pk']
    listing = get_object_or_404(Listing, pk=pk)
    
    listing.count = listing.count + 1
    listing.save()
    print(listing.count)
    
    voter = request.user
    upvote_instance = Upvotes.objects.create(voter=voter, listing_upvoted=listing)
    
    return HttpResponse(listing.count)
     
    

@csrf_exempt
def downvote(request):
    """Take the pk from the ajax call and use to find listing id. Delete that record. Also at the same time decrease the count by one. (opposote of upvote view)"""
    
    pk = request.POST['pk']
    listing = get_object_or_404(Listing, pk=pk)
    
    listing.count = listing.count - 1
    listing.save()
    
    voter = request.user
    downvote_instance = Upvotes.objects.filter(voter=voter, listing_upvoted=listing).delete()
    
    return HttpResponse(listing.count)


from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponseForbidden, HttpResponse
from .forms import NewListing
from .models import Listing

# Create your views here.

def create_listing(request):
    if not request.user.is_authenticated:
        return redirect('login')
    else:
        try:
            if request.method == "POST":
                form = NewListing(request.POST, request.FILES)
                if form.is_valid():
                    listing = form.save(commit=False)
                    listing.owner = request.user
                    listing.save()
                    print("saved form")
                    return redirect('profile')
            else:
                form = NewListing()

        except:
            print("end error")
            return HttpResponseForbidden()

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
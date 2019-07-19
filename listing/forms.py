from django import forms
from .models import Listing, ListingArchive, Upvotes


class UploadUpvotes(forms.ModelForm):
    class Meta:
        model = Upvotes
        fields = ['voter', 'listing_upvoted']

class ImageUploadForm(forms.Form):
    """Image upload form."""
    image = forms.ImageField()

class NewListingArchive(forms.ModelForm):
    class Meta:
        model = ListingArchive
        fields = ('title', 'content', 'contact', 'image', 'tag', 'can_offer')

class NewListing(forms.ModelForm):
    class Meta:
        model = Listing
        exclude = ['created_by']
        # exclude user from here so it doesnt come through as a field to be filled in in the html
        

"""
comment out while fixing forms...

class NewListing(forms.Form):
   
    name = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'name'}))
    description = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'description'}))
    image = forms.ImageField()
    
    class Meta:
        model = Listing
        fields = ['name', 'description', 'image']
"""
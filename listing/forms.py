from django import forms
from .models import Listing, ListingArchive


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
        exclude = ['user']
        # exclude user from here so it doesnt come through as a field to be filled in in the html
        


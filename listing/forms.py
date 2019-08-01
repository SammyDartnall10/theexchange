from django import forms
from .models import Listing, Upvotes


class UploadUpvotes(forms.ModelForm):
    class Meta:
        model = Upvotes
        fields = ['voter', 'listing_upvoted']

class ImageUploadForm(forms.Form):
    """Image upload form."""
    image = forms.ImageField()


class NewListing(forms.ModelForm):
    class Meta:
        model = Listing
        exclude = ['created_by', 'count', 'tag']
        # exclude user from here so it doesnt come through as a field to be filled in in the html
        

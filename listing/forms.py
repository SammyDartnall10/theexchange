from django import forms
from .models import Listing

class NewListing(forms.Form):
    """
    To go into html for a new listing
    """
    name = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'name'}))
    description = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'description'}))
    image = forms.ImageField()
    
    class Meta:
        model = Listing
        fields = ['name', 'description', 'image']

class ImageUploadForm(forms.Form):
    """Image upload form."""
    image = forms.ImageField()
    
    
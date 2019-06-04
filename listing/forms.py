from django import forms
from .models import Listing

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

class NewListing(forms.ModelForm):
    class Meta:
        model = Listing
        fields = ('title', 'content', 'image', 'tag')


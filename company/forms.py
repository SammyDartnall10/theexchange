from django import forms
from .models import CompanyDetail

class CompanyDetailForm(forms.ModelForm):
    class Meta:
        model = CompanyDetail
        exclude = ['created_by']
        #fields = ('industry', 'contact_email', 'about_us', 'logo')
        # exclude user from here so it doesnt come through as a field to be filled in in the html
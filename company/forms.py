from django import forms
from .models import CompanyDetail, CompanyReview

class CompanyDetailForm(forms.ModelForm):
    class Meta:
        model = CompanyDetail
        exclude = ['created_by']
        #fields = ('industry', 'contact_email', 'about_us', 'logo')
        # exclude user from here so it doesnt come through as a field to be filled in in the html
        
class CompanyReviewForm(forms.ModelForm):
    class Meta:
        model = CompanyReview
        exclude = ['created_by', 'company_reviewed', 'date_created']
        #fields = ['created_by', 'company_reviewed', 'content', 'rating', 'date_created']
        

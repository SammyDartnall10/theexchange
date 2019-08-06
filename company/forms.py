from django import forms
from .models import CompanyDetail, CompanyReview

class CompanyDetailForm(forms.ModelForm):
    class Meta:
        model = CompanyDetail
        exclude = ['created_by', 'overall_rating']
       
        
        
class CompanyReviewForm(forms.ModelForm):
    class Meta:
        model = CompanyReview
        exclude = ['created_by', 'company_reviewed', 'date_created']
        
        

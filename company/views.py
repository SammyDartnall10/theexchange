
from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponseForbidden, HttpResponse
from django.contrib import auth, messages
from datetime import datetime
from django.db.models import Avg, Count
from .forms import CompanyDetailForm, CompanyReviewForm
from .models import CompanyDetail, CompanyReview

# Create your views here.


def edit_company(request, pk):
    """
    When logged in, renders a form that the user can then use to edit the company specific details held about their company. Initially this data is the default values or blank as set in the model - these values are edited by the user once they have signed up/logged in. Note - the company will not apprear in searches until the user updates the company info for the first time - this stops loads of default businesses being shown to others. 
    Note - different to editing personal details - company and person are two different entities here - see ReadMe. 
    """
    company = get_object_or_404(CompanyDetail, pk=pk)
    if request.user.is_authenticated and request.user == company.created_by or request.user.is_superuser: 
        if request.method == "POST":
            form = CompanyDetailForm(request.POST, request.FILES, instance=company)
            if form.is_valid():
                company = form.save()
                return redirect('profile')        
        else:
            form = CompanyDetailForm(instance=company)
    else: 
        return HttpResponseForbidden()
        
    return render(request, 'edit_company.html', {'form': form})
    
    

def filtered_company(request):
    """
    search based on text input - returns companies as a list or error message if no matching results. icontain makes the search case insensitive. 
    """
    if request.method =="POST":
        search_criteria = request.POST.get('search-company')
        companies = CompanyDetail.objects.filter(business_name__icontains=search_criteria)
        if companies:
            return render(request, "filtered_company.html", {'companies': companies})
        else :
            messages.success(request, "Sorry, no matching results! Please try again")
            return render(request, "filtered_company.html", {'companies': companies})
    else:
        return render(request, "error.html")
        
        

def company_detail(request, pk):
    """
    View that is only accessable as the logged in user - can go to edit pages from here
    """
    company = get_object_or_404(CompanyDetail, pk=pk)
    company_form = CompanyReviewForm(request.POST, request.FILES)
    reviews = CompanyReview.objects.filter(company_reviewed = company)
    return render(request, "company_detail.html", {'company': company, 'company_form': company_form, 'reviews': reviews})
    
    
def company_search(request, company_name):
    """
    search for company based on name - display info that cannot be edited (read only)
    """
    
    company = CompanyDetail.objects.get(business_name__contains=company_name)
    company_form = CompanyReviewForm(request.POST, request.FILES)
    reviews = CompanyReview.objects.filter(company_reviewed = company)
    
    return render(request, "view_company.html", {'company': company, 'company_form': company_form, 'reviews': reviews})
    
 
def add_company_review(request, company):
    """
    return paage with confirmation reveiw has been successful.  
    """
    if request.method == 'POST':
        company_form = CompanyReviewForm(request.POST, request.FILES)
        if company_form.is_valid():
            review = company_form.save(commit=False)
            review.company_reviewed=CompanyDetail.objects.get(business_name = company)
            review.created_by = request.user  # The logged-in user - re-fill in this field automatically
            review.save()
            
            company = get_object_or_404(CompanyDetail, business_name = company)
            company_form = CompanyReviewForm(request.POST, request.FILES)
            reviews = CompanyReview.objects.filter(company_reviewed = company)
            avg_rating = CompanyReview.objects.filter(company_reviewed = company).aggregate(Avg('rating'))
            
            messages.success(request, "You have successfully left a review!")
            return render(request, "view_company.html", {'company': company, 'company_form': company_form, 'reviews': reviews, 'avg_rating': avg_rating})
    else:
        company_form = CompanyReviewForm()
        
    return redirect('/') 
    
 
def create_company(request):
    """
    Creates a new company when the user creates a new account. 
    """
    if request.method == 'POST':
        form = CompanyDetailForm(request.POST, request.FILES)
        if form.is_valid():
            company = form.save(commit=False)
            company.created_by = request.user  # The logged-in user - re-fill in this field automatically
            company.save()
            return redirect('profile')
    else:
        form = CompanyDetailForm()
    return render(request, 'new_company.html', {'form': form})
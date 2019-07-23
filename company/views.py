
from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponseForbidden, HttpResponse
from django.contrib import auth, messages
from datetime import datetime
from django.db.models import Avg, Count
from .forms import CompanyDetailForm, CompanyReviewForm
from .models import CompanyDetail, CompanyReview

# Create your views here.

def create_company(request):
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

def edit_company(request, pk):
    company = get_object_or_404(CompanyDetail, pk=pk)
    if request.user.is_authenticated and request.user == company.created_by or request.user.is_superuser: 
        if request.method == "POST":
            form = CompanyDetailForm(request.POST, request.FILES, instance=company)
            if form.is_valid():
                company = form.save()
                return redirect('/')        
        else:
            form = CompanyDetailForm(instance=company)
    else: 
        return HttpResponseForbidden()
        
    return render(request, 'edit_company.html', {'form': form})
    #rendering the createnew file as its the same- wil display the info already saved and then save over with the edits. Linked in URLs
    
def company_detail(request, pk):
    """
    Create a view that returns a single Post object based on the post ID (pk) and render it to the 'postdetail.html' template.
    Or return a 404 error if the post is not found
    """
    company = get_object_or_404(CompanyDetail, pk=pk)
    return render(request, "company_detail.html", {'company': company})

def filtered_company(request):
    """
    search based on text input - returns companies
    """
    if request.method =="POST":
        search_criteria = request.POST.get('search-company')
        print(search_criteria)
        companies = CompanyDetail.objects.filter(business_name__contains=search_criteria)
        print(type(companies))
        return render(request, "filtered_company.html", {'companies': companies})
    else:
        return HttpResponse("Sorry, no results for that business - please try again")
        
        #TODO add display on average rating in list.. 

    
def company_search(request, company_name):
    """
    search for comanpy based on name - display info that cant be editied (read only)
    """
    
    company = CompanyDetail.objects.get(business_name__contains=company_name)
    company_form = CompanyReviewForm(request.POST, request.FILES)
    reviews = CompanyReview.objects.filter(company_reviewed = company)
    #avg_rating = CompanyReview.objects.filter(company_reviewed = company).aggregate(Avg('rating'))
    
    print(company)
    #print(avg_rating)
    #print(type(avg_rating))
    
    return render(request, "view_company.html", {'company': company, 'company_form': company_form, 'reviews': reviews})
    
 
def add_company_review(request, company):
    """return page with new review added """
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
 
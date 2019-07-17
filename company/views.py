
from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponseForbidden, HttpResponse
from django.contrib import auth, messages
from datetime import datetime, timezone
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
    
def company_search(request):
    """
    search for comanpy based on name
    """
    if request.method =="POST":
        search_criteria = request.POST.get('search-company')
        company = CompanyDetail.objects.get(business_name__contains=search_criteria)
        company_form = CompanyReviewForm(request.POST, request.FILES)
        return render(request, "view_company.html", {'company': company, 'company_form': company_form})
    else:
        return HttpResponse("Sorry, we appear to be having a slight issue at the moment - please try again")
        
        
        
 
def add_company_review(request, company):
    if request.method == 'POST':
        company_form = CompanyReviewForm(request.POST, request.FILES)
        if company_form.is_valid():
            review = company_form.save(commit=False)
            review.company_reviewed=CompanyDetail.objects.get(business_name = company)
            review.created_by = request.user  # The logged-in user - re-fill in this field automatically
            review.save()
            company = get_object_or_404(CompanyDetail, business_name = company)
            messages.success(request, "You have successfully left a review!")
            return render(request, "company_detail.html", {'company': company})
    else:
        company_form = CompanyReviewForm()
        
    return redirect('/')  
 
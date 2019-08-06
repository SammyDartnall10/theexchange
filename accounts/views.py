
# Create your views here. - Have come from forms.py

from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.http import HttpResponseForbidden, HttpResponse
from django.template.context_processors import csrf
from django.contrib import auth, messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib.auth import get_user
from accounts.forms import UserLoginForm, UserRegistrationForm, MakePaymentForm
from django.conf import settings
from listing.models import Listing
from django.db.models import Avg, Count
from company.models import CompanyDetail, CompanyReview
from company.forms import CompanyDetailForm

import datetime
import stripe


def about(request):
    """Return the index.html file"""
    return render(request, 'index.html')

@login_required
def logout(request):
    """Log the user out"""
    auth.logout(request)
    return redirect(reverse('index'))


def login(request):
    """Return a login page"""
    if request.user.is_authenticated:
        return redirect(reverse('index'))
    if request.method == "POST":
        login_form = UserLoginForm(request.POST)

        if login_form.is_valid():
            user = auth.authenticate(username=request.POST['username'],
                                    password=request.POST['password'])

            if user:
                auth.login(user=user, request=request)
                return redirect(reverse('profile'))
            else:
                login_form.add_error(None, "Your username or password is incorrect")
    else:
        login_form = UserLoginForm()
    return render(request, 'login.html', {'login_form': login_form})
    

stripe.api_key = settings.STRIPE_SECRET
        
def register(request):
    """
    Rego page is made up of the standard Django user auth, and stripe payments form. Reason for having it in one is to stop half the process going through, ie, say the user details are correct but the card payment fails, an account wont be created. Also stops the flipside happening - eg stripe payments going through but the account not being created. 
    Company creation is triggered when the user registers, but details for the company are not in this form/view, to reduce the burden on  the user/make the forms less overwhelming (noone like filling out 20 fields for a simple signup! Would rather do it later)
    """
    if request.user.is_authenticated:
        return redirect(reverse('profile'))

    if request.method == "POST":
        registration_form = UserRegistrationForm(request.POST)
        payment_form = MakePaymentForm(request.POST)
        company_form = CompanyDetailForm(request.POST)
        
        if registration_form.is_valid() and payment_form.is_valid():
            
            try: 
                customer = stripe.Charge.create(
                    amount = 499,
                    currency = "CAD",
                    description = registration_form.cleaned_data['email'],
                    card = payment_form.cleaned_data['stripe_id'], 
                    )
               
                messages.success(request, "Payment made")
                
            except stripe.error.CardError:
                messages.error(request, "Your card was declined!")
                
            
            print(request.POST['username'])
            print(request.POST['password1'])
            
            registration_form.save()
            
            
            user = auth.authenticate(username=request.POST['username'],
                                    password=request.POST['password1'])
            print(user)
            
            
            
            if user:
                auth.login(user=user, request=request)
                messages.success(request, "You have successfully registered")
                
                if company_form.is_valid():
                    company = company_form.save(commit=False)
                    company.created_by = request.user # The logged-in user - re-fill in this field automatically
                    company_form.save()
                
                else:
                    messages.error(request, "CompanyDetailForm not valid")
                
                return redirect(reverse('profile'))
            
            else:
                messages.error(request, "Unable to register your account at this time")
                    
                
        else:
            messages.error(request, "Form not valid") 
            
    else:
        registration_form = UserRegistrationForm(request.POST)
        payment_form = MakePaymentForm(request.POST)
        company_form = CompanyDetailForm(request.POST)

        
    return render(request, 'register.html', {'registration_form': registration_form, "payment_form": payment_form, 'company_form': company_form, "publishable": settings.STRIPE_PUBLISHABLE})


def profile(request):
    """The user's profile page"""
    user = User.objects.get(email=request.user.email)
    listings = Listing.objects.filter(created_by = request.user)
    
    if CompanyDetail.objects.get(created_by = request.user):
        company = CompanyDetail.objects.get(created_by = request.user)
        reviews = CompanyReview.objects.filter(company_reviewed = company)
        
    else: 
        company = CompanyDetail.objects.get(created_by = 'admin2')
        
    return render(request, 'profile.html', {"profile": user, "listings": listings, "company": company, 'reviews': reviews})                    



def edit_profile(request, pk):
    """
    Only name, username, an email and password are editable here. Id is hidden, as it is a forgein key to other tables- changing it would result in discrepancies in data records. 
    """
    user = get_object_or_404(User, pk=pk)
    print(user.username)
    if request.user.is_authenticated and request.user == request.user or request.user.is_superuser: 
        if request.method == "POST":
            form = UserRegistrationForm(request.POST, request.FILES, instance=user)
            if form.is_valid():
                listing = form.save()
                return redirect('profile.html')        
        else:
            form = UserRegistrationForm(instance=user)
    else: 
        return HttpResponseForbidden()
        
    return render(request, 'edit_profile.html', {'user': user, "form":form})

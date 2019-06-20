
# Create your views here. - Have come from forms.py

from django.shortcuts import render, redirect, reverse
from django.template.context_processors import csrf
from django.contrib import auth, messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from accounts.forms import UserLoginForm, UserRegistrationForm, MakePaymentForm
from django.conf import settings
import datetime
import stripe

def about(request):
    """Return the index.html file"""
    return render(request, 'index.html')

@login_required
def logout(request):
    """Log the user out"""
    auth.logout(request)
    messages.success(request, "You have successfully been logged out")
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
            messages.success(request, "You have successfully logged in!")

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
    """Render the registration page"""
    if request.user.is_authenticated:
        return redirect(reverse('profile'))

    if request.method == "POST":
        registration_form = UserRegistrationForm(request.POST)
        payment_form = MakePaymentForm(request.POST)

        if registration_form.is_valid():
                try: 
                    customer = stripe.Charge.create(
                        amount = 499,
                        currency = "USD",
                        description = registration_form.cleaned.data['email'],
                        card = payment_form.cleaned_data['stripe_id'], 
                        )
                        
                    registration_form.save()
                    
                    user = auth.authenticate(username=request.POST['username'],
                                            password=request.POST['password1'])
                    
                    if user:
                        auth.login(user=user, request=request)
                        messages.success(request, "You have successfully registered")
                    else:
                        messages.error(request, "Unable to register your account at this time")
                    
                    #redirect('/profile')
                    
                except stripe.CardError:
                    registration_form.add_error("The card has been declined")
                
    else:
        registration_form = UserRegistrationForm(request.POST)
        payment_form = MakePaymentForm(request.POST)

        
    return render(request, 'register.html', {'registration_form': registration_form})


def profile(request):
    """The user's profile page"""
    user = User.objects.get(email=request.user.email)
    return render(request, 'profile.html', {"profile": user})
    
#--------------------------------------------------------------------------------------------------------------------------------
"""args = {}
    args.update(csrf(request))
    args['form'] = registration_form
    args['publishable'] = settings.STRIPE_PUBLISHABLE
    args['months'] = range(1, 12)
    args['years'] = range(2011, 2036)
    args['soon'] = datetime.date.today() + datetime.timedelta(days=30)
"""
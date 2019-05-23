from django.shortcuts import render

# Create your views here.

def index(request):
    """Return the index.html file"""
    return render(request, 'index.html')
    
    
#import the forms and say signup = theNameOfTheFormInForms.py 
#eg from .forms import MakePaymentForm, OrderForm

#then say what you want to do with it

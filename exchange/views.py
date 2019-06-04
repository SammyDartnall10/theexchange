from django.shortcuts import render

# Create your views here.

def exchange(request):
    """Return the about.html file"""
    return render(request, 'exchange.html')

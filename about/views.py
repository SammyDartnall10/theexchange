from django.shortcuts import render

# Create your views here.

def about(request):
    """Return the about.html file"""
    return render(request, 'about.html')

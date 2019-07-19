"""
ACCOUNT APP

testproject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls')"""
    
    
from django.urls import path, include
from .views import create_listing, get_listings, edit_listing, listing_detail, filtered_listings, view_listing, testcall
#new_listing

urlpatterns = [
    path('', create_listing, name='listing'),
    path('<pk>/edit_listing', edit_listing, name='edit_listing'),
    path('<pk>/detail', listing_detail, name='listing_detail'),
    path('exchange', get_listings, name='exchange'),
    path('exchange/results', filtered_listings, name='filtered_results'),
    path('<pk>/view_listing', view_listing, name='view_listing'),
    path('<pk>/my-ajax-test/', testcall, name='testcall'),
    #path('new/', new_listing, name='new_listing'),
]
    

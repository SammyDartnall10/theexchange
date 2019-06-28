"""
BUSEX TOP LEVEL

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
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from landing import urls as urls_landing
from about import urls as urls_about
from exchange import urls as urls_exchange
from accounts import urls as urls_account
from listing import urls as urls_listing
from company import urls as urls_company
from django.views.static import serve
from django.conf import settings
from .settings import MEDIA_ROOT


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('landing.urls')),
    path('about/', include('about.urls')),
    path('exchange', include('exchange.urls')),
    path('accounts/', include('accounts.urls')),
    path('listing/', include('listing.urls')),
    path('company/', include('company.urls')),
    path('media/<path:path>', serve, {'document_root': settings.MEDIA_ROOT }),
]

#then pull through the views and use the urls to call the functions - that then renders the template
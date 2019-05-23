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
from account import urls as urls_account


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('landing.urls')),
    path('about/', include('about.urls')),
    path('account/', include('account.urls'))
]

#then pull through the views and use the urls to call the functions - that then renders the template
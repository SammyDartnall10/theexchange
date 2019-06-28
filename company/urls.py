from django.urls import path, include
from .views import edit_company, company_detail

urlpatterns = [
    path('<pk>/company_detail', company_detail, name='company_detail'),
    path('<pk>/edit_company', edit_company, name='edit_company'),
    ]
from django.urls import path, include
from .views import edit_company, company_detail, company_search, add_company_review, filtered_company

urlpatterns = [
    path('<pk>/company_detail', company_detail, name='company_detail'),
    path('<pk>/edit_company', edit_company, name='edit_company'),
    path('filtered_company', filtered_company, name='filtered_company'),
    path('<company_name>/company_search', company_search, name='company_search'),
    path('<company>/add_review', add_company_review, name='add_company_review')
    ]
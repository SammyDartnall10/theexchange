from django.contrib import admin
from .models import CompanyDetail, CompanyReview, ReviewCompany

# Register your models here.
admin.site.register(CompanyDetail)
admin.site.register(CompanyReview)
admin.site.register(ReviewCompany)
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.db.models import Avg

# Create your models here.
        
class CompanyDetail(models.Model):    
    INDUSTRY = (
            ('Agriculture, forestry, fishing and hunting','Agriculture, forestry, fishing and hunting'),
            ('Construction','Construction'),
            ('Manufacturing','Manufacturing'),
            ('Transportation equipment manufacturing', 'Transportation equipment manufacturing'),
            ('Service industries', 'Service industries'),
            ('Wholesale Trade', 'Wholesale Trade'),
            ('Retail Trade', 'Retail Trade'),
            ('Transportation and warehousing', 'Transportation and warehousing'),
            ('Information and cultural industries', 'Information and cultural industries'),
            ('Finance and insurance', 'Finance and insurance'),
            ('Real estate and rental and leasing', 'Real estate and rental and leasing'),
            ('Professional, scientific, and technical services', 'Professional, scientific, and technical services'),
            ('Management of companies and enterprises', 'Management of companies and enterprises'),
            ('Administrative and support, waste management and remediation services', 'Administrative and support, waste management and remediation services'),
        )
        
    business_name = models.CharField(max_length=254, null=True, default="Business Name", blank=True)
    industry = models.CharField(max_length=254, null=True, choices=INDUSTRY, default="Please pick an industry", blank=True)
    contact_email = models.EmailField(default="email@email.com", null=True, blank=True)
    about_us = models.TextField(null=True, default="Information about your company - where you're from, what you do!", blank=True)
    street_address = models.TextField(null=True, default="Business Address", blank=True)
    city = models.CharField(max_length=254, null=True, default="Toronto", blank=True)
    country = models.CharField(max_length=254, null=True, default="Canada", blank=True)
    logo = models.ImageField(upload_to='images', null=True, blank=True)
    created_by = models.ForeignKey(User, null=True, default="1", on_delete=models.SET_DEFAULT)
    @property
    def average_review(self):
        reviews = self.companyreview_set.all()
        avg_rating = reviews.aggregate(Avg('rating'))
        return avg_rating
    
    #avg_rating = models.IntegerField(CompanyReview.objects.filter(company_reviewed = company).aggregate(Avg('rating')))
    
    
class CompanyReview(models.Model):
    RATINGS = (
        (1,'1'),
        (2,'2'),
        (3,'3'),
        (4,'4'),
        (5,'5'),
        )
    
    created_by = models.ForeignKey(User, null=True, default=1, on_delete=models.SET_DEFAULT)
    company_reviewed = models.ForeignKey(CompanyDetail, null=True, default="Default Business Name", on_delete=models.SET_DEFAULT)
    content = models.TextField(max_length=254, null=True, default="Review Content", blank=False)
    rating = models.IntegerField(choices=RATINGS, blank=False)
    date_created = models.DateTimeField(blank=True, null=True, default=timezone.now)
    

from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

# Create your models here.
        
class CompanyDetail(models.Model):    
    INDUSTRY = (
            ('AG', 'Agriculture, forestry, fishing and hunting'),
            ('CN', 'Construction'),
            ('MG', 'Manufacturing'),
            ('TR', 'Transportation equipment manufacturing'),
            ('SI', 'Service industries'),
            ('WT', 'Wholesale Trade'),
            ('RT', 'Retail Trade'),
            ('TW', 'Transportation and warehousing'),
            ('IC', 'Information and cultural industries'),
            ('FI', 'Finance and insurance'),
            ('RE', 'Real estate and rental and leasing'),
            ('PS', 'Professional, scientific, and technical services'),
            ('MA', 'Management of companies and enterprises'),
            ('AD', 'Administrative and support, waste management and remediation services'),
        )
        
    business_name = models.CharField(max_length=254, null=True, default="Business Name", blank=True)
    industry = models.CharField(max_length=254, null=True, choices=INDUSTRY, default="Please pick an industry", blank=True)
    contact_email = models.EmailField(default="email@email.com", null=True, blank=True)
    about_us = models.TextField(null=True, default="Information about your company - where you're from, what you do!", blank=True)
    address = models.TextField(null=True, default="Business Address", blank=True)
    logo = models.ImageField(upload_to='images', null=True, blank=True)
    created_by = models.ForeignKey(User, null=True, default="1", on_delete=models.SET_DEFAULT)
    
    
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
    

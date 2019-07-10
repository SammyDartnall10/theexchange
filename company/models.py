from django.db import models
from django.contrib.auth.models import User

# Create your models here.
        
class CompanyDetail(models.Model):    
    INDUSTRY = (
            ('Agriculture, forestry, fishing and hunting', 'Agriculture, forestry, fishing and hunting'),
            ('Construction', 'Construction'),
            ('Manufacturing', 'Manufacturing'),
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
        
    industry = models.CharField(max_length=254, null=True, choices=INDUSTRY, default="Please pick an industry", blank=True)
    contact_email = models.EmailField(default="email@email.com", null=True, blank=True)
    about_us = models.CharField(max_length=254, null=True, default="Information about your company - where you're from, what you do!", blank=True)
    address = models.CharField(max_length=254, null=True, default="Business Address", blank=True)
    image = models.ImageField(upload_to='images', null=True, blank=True)
    created_by = models.ForeignKey(User, null=True, default=1, on_delete=models.SET_DEFAULT)
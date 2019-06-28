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
            ('Mining, quarrying, and oil and gas extraction', 'Mining, quarrying, and oil and gas extraction'),
        )
        
    industry = models.CharField(max_length=254, choices=INDUSTRY, default="Industry")
    contact_email = models.EmailField(default="contact email")
    about_us = models.CharField(max_length=254, default="Information about your company - where you're from, what you do!")
    logo = models.ImageField(upload_to='images', null=False)
    created_by = models.ForeignKey(User, null=False, default=1, on_delete=models.SET_DEFAULT)
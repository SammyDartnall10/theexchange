from django.db import models
from django.contrib.auth.models import User

# Create your models here.
# Custom Model for use in registration form

class CustomUser(models.Model):
    username = models.CharField(max_length=255)
    email = models.EmailField()
    
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
        
    industry = models.CharField(max_length=1, choices=INDUSTRY, default="Industry")
    contact_email = models.EmailField(default="contact email")
    about_us = models.CharField(max_length=254, default="Information about your company - where you're from, what you do!")
    logo = models.ImageField(upload_to='images', null=False)
    created_by = models.ForeignKey(User, null=False, default=1, on_delete=models.SET_DEFAULT)
    
"""
from django.db import models
from products.models import Product

# Create your models here.
class Order(models.Model):
    full_name = models.CharField(max_length=50, blank=False)
    phone_number = models.CharField(max_length=20, blank=False)
    country = models.CharField(max_length=40, blank=False)
    postcode = models.CharField(max_length=20, blank=True)
    town_or_city = models.CharField(max_length=40, blank=False)
    street_address1 = models.CharField(max_length=40, blank=False)
    street_address2 = models.CharField(max_length=40, blank=False)
    county = models.CharField(max_length=40, blank=False)
    date = models.DateField()
    
    def __str__(self):
        return "{0}-{1}-{2}".format(self.id, self.date, self.full_name)
        
class OrderLineItem(models.Model):
    order = models.ForeignKey(Order, null=False)
    product = models.ForeignKey(Product, null=False)
    quantity = models.IntegerField(blank=False)
    
    def __str__(self):
        return "{0} {1} {2}".format(self.quantity, self.product.name, self.product.price)
        
"""
    
    
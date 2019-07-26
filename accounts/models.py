from django.db import models
from django.contrib.auth.models import User

# Create your models here.
# Custom Model for use in registration form

class CustomUser(models.Model):
    username = models.CharField(max_length=255)
    email = models.EmailField()
    first_name = models.CharField(max_length=255, default="first name")
    last_name = models.CharField(max_length=255, default="last name")
    
    
    
from django.db import models

# Create your models here.
# Custom Model for use in registration form

class CustomUser(models.Model):
    username = models.CharField(max_length=255)
    email = models.EmailField()
    stripe_id = models.CharField(max_length=255)
    
    
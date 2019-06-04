from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Listing(models.Model):
    name = models.CharField(max_length=254, default="")
    description = models.TextField()
    image = models.ImageField(upload_to='images', null=False)
    
    def __str__(self):
        return self.name

class ExampleModel(models.Model):
    model_pic = models.ImageField(upload_to = 'pic_folder/', default = 'pic_folder/None/no-img.jpg')
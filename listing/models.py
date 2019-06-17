from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Listing(models.Model):
    title = models.CharField(max_length=254, default="")
    content = models.TextField()
    image = models.ImageField(upload_to='images', null=False)
    contact = models.EmailField()
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)
    tag = models.TextField()
    
    def __str__(self):
        return self.title
        
#TODO add in email validator

#class ExampleModel(models.Model):
#    model_pic = models.ImageField(upload_to = 'pic_folder/', default = 'pic_folder/None/no-img.jpg')

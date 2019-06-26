from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Listing(models.Model):

    title = models.CharField(max_length=254, default="Listing Title")
    content = models.TextField()
    image = models.ImageField(upload_to='images', null=False)
    contact = models.EmailField(default="email@email.com")
    created_by = models.ForeignKey(User, related_name='listings', null=False, default=1, on_delete=models.SET_DEFAULT)
    tag = models.TextField()
    can_offer = models.TextField(default=1)
         
    def __str__(self):
        return self.title

#TODO add in email validator

#class ExampleModel(models.Model):
#    model_pic = models.ImageField(upload_to = 'pic_folder/', default = 'pic_folder/None/no-img.jpg')

from django.db import models
from django.contrib.auth.models import User
from company.models import CompanyDetail
from django.db.models import Count

# Create your models here.
class ListingArchive(models.Model):

    title = models.CharField(max_length=254, default="Listing Title")
    content = models.TextField()
    image = models.ImageField(upload_to='images', null=False)
    contact = models.EmailField(default="email@email.com")
    created_by = models.ForeignKey(User, related_name='listings', null=False, default=1, on_delete=models.SET_DEFAULT)
    tag = models.TextField()
    can_offer = models.TextField(default=1)
         
    def __str__(self):
        return self.title
        
class Listing(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=254, default="Listing Title")
    content = models.TextField("What are you looking for? Be as detailed as possible!")
    image = models.ImageField(upload_to='images', null=False)
    contact = models.EmailField(default="The best email for people to contact you at")
    tag = models.TextField()
    can_offer = models.TextField(default="Please detail the things you can offer in return as single words, eg catering, photography")
    created_by = models.ForeignKey(User, null=False, default=1, on_delete=models.SET_DEFAULT)
    #total_upvotes = models.IntegerField(default=self.upvotes, blank=False)
    @property
    def upvotes(self):
        count_upvotes = self.upvotes_set.all()
        total_count = count_upvotes.count()
        return total_count
    #archive = models.BooleanField() figure this out later...
    #user added in here to create a location to store the values with everything in the database


 

    def __unicode__(self):
        return self.title;

class Upvotes(models.Model):
    voter = models.ForeignKey(User, null=False, default=1, on_delete=models.SET_DEFAULT)
    listing_upvoted = models.ForeignKey(Listing, null=True, default="Default Business Name", on_delete=models.SET_DEFAULT)

#TODO add in email validator

#class ExampleModel(models.Model):
#    model_pic = models.ImageField(upload_to = 'pic_folder/', default = 'pic_folder/None/no-img.jpg')

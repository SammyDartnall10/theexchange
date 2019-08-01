from django.db import models
from django.contrib.auth.models import User
from company.models import CompanyDetail
from django.db.models import Count
#from votes.managers import VotableManager

# Create your models here.
#class Recommendation(models.Model):
#    topic = models.ForeignKey(Topic)
#    user = models.ForeignKey(User)
#    title = models.CharField(max_length=300)
#    votes = VotableManager()

#    def get_total_votes(self):
#        total = self.votes.count()
#        return int(total)

#class ListingTest(models.Model):
#    id = models.AutoField(primary_key=True)
#    title = models.CharField(max_length=254, default="Listing Title")
#    content = models.TextField("What are you looking for? Be as detailed as possible!")
#    image = models.ImageField(upload_to='images', null=False)
#    contact = models.EmailField(default="The best email for people to contact you at")
#    tag = models.TextField()
#    can_offer = models.TextField(default="Please detail the things you can offer in return as single words, eg catering, photography")
#    created_by = models.ForeignKey(User, null=False, default=1, on_delete=models.SET_DEFAULT)
#    votes = VotableManager()
#    def get_total_votes(self):
#        total = self.votes.count()
#        return int(total)
#    
#    def __str__(self):
#        return self.title
        
class Listing(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField("Listing Title.. As it sounds.. what are you looking for?", max_length=254, default= "Web Design, Photography, Cake, Puppies.. (we can dream)")
    content = models.TextField("What are you looking for? Be as detailed as possible!")
    image = models.ImageField("Pro tip: Square-ish pics work best.. we wont crop your photos to suit a set window, but that does mean rectangles come out looking a bit funny!", upload_to='images', null=False)
    contact = models.EmailField(default="The best email for people to contact you at")
    can_offer = models.TextField("What are all the really awesome things you can offer in return? Enter as single words or a statement", default="Use keywords, such as photography, graphic design, carpentry, dog sitting... ")
    created_by = models.ForeignKey(User, null=False, default=1, on_delete=models.SET_DEFAULT)
    count = models.IntegerField(default=0)
    @property
    def upvotes(self):
        count_upvotes = self.upvotes_set.all()
        total_count = count_upvotes.count()
        
        return total_count
    
    def __str__(self):
        return self.title


    #archive = models.BooleanField() figure this out later...
    #user added in here to create a location to store the values with everything in the database



class Upvotes(models.Model):
    voter = models.ForeignKey(User, null=False, default=1, on_delete=models.SET_DEFAULT)
    listing_upvoted = models.ForeignKey(Listing, null=True, default="Default Business Name", on_delete=models.SET_DEFAULT)
    
    def __int__(self):
        return self.id



#class ExampleModel(models.Model):
#    model_pic = models.ImageField(upload_to = 'pic_folder/', default = 'pic_folder/None/no-img.jpg')

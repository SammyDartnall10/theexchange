from django.db import models
from django.contrib.auth.models import User
from company.models import CompanyDetail
from django.db.models import Count

        
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
        
    #Credit to my mentor Aaron Sinnott for helping me with the upvotes property/how to set the property as a function. 
    #Have learned in the process that you can display the result of this function, but it doesnt act like an integer. Tried converting to an int() in views.py for ordering with no luck. Have put in the count property instead to based the ranking/upvotes on. 
    
    def __str__(self):
        return self.title



class Upvotes(models.Model):
    voter = models.ForeignKey(User, null=False, default=1, on_delete=models.SET_DEFAULT)
    listing_upvoted = models.ForeignKey(Listing, null=True, default="Default Business Name", on_delete=models.SET_DEFAULT)
    
    def __int__(self):
        return self.id



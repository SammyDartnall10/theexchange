from django.contrib import admin
from .models import Listing, Upvotes

# Register your models here.
 
admin.site.register(Upvotes)

class ListingAdmin(admin.ModelAdmin):
	readonly_fields = ["upvotes"]

admin.site.register(Listing, ListingAdmin)



from django.contrib import admin
from .models import Listing, Upvotes

# Register your models here.
admin.site.register(Listing)
admin.site.register(Upvotes)
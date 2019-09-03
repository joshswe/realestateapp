from django.contrib import admin
from .models import Listing

# You can customize the columns that you want to display in the Listings admin page in this class
class ListingAdmin(admin.ModelAdmin):
    list_display = ('id','title','is_published','price','list_date','realtor')
    list_display_links = ('id','title')
    list_filter = ('realtor',) # Filter the listings by realtor
    list_editable = ('is_published',)
    search_fields = ('title','description','address','city','state','zipcode','price')
    list_per_page = 25



# Register your models here.
admin.site.register(Listing,ListingAdmin) # This line allows you to add admin user in the admin page for Listing Model
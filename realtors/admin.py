from django.contrib import admin
from .models import Realtor


# You can customize the columns that you want to display in the Listings admin page in this class
class RealtorAdmin(admin.ModelAdmin):
    list_display = ('id','name','email','hire_date')
    list_display_links = ('id','name')
    search_fields = ('name',)
    list_per_page = 25


# Register your models here.
admin.site.register(Realtor, RealtorAdmin) # This line allows you to add admin user in the admin page for Listing Model


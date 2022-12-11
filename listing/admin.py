from django.contrib import admin

from listing.models import listing

class ListingList(admin.ModelAdmin):
    list_display=('property_type','AgentCity_id','Location','property_title','desc','rental_price','land_area','unit','bedroom','bathroom','submitOn','img','img2','img3','user_id')
    
# Register your models here.
admin.site.register(listing,ListingList)


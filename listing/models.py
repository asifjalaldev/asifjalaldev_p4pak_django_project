import operator
import os
from django.db import models
from django.http import HttpResponse
from accounts.queryDebugger import query_debugger
from agentDirectory.models import AgentCity
from django.contrib.auth.models import User

# Create your models here.
class listing(models.Model):
    purpose=models.CharField(verbose_name='Purpose(rent or sale)' ,max_length=30, blank= True)
    property_type=models.CharField(verbose_name='Property Type(plat or house)' ,max_length=30, blank=True)
    AgentCity_id=models.ForeignKey(AgentCity, on_delete=models.SET_NULL,null=True, related_name='relatedCity')
    Location=models.CharField(max_length=30, blank=True)
    property_title=models.CharField(max_length=100, blank=True)
    desc=models.TextField(verbose_name='Description' ,blank=True)
    rental_price= models.CharField(max_length=30, blank=True)
    land_area=models.CharField(max_length=50, blank= True)
    unit=models.CharField(max_length=30, blank= True)
    bedroom=models.IntegerField(verbose_name='BedRooms(leave blank for plat)' , blank= True)
    bathroom=models.IntegerField(verbose_name='BathRooms(leave blank for plat)' ,blank=True)
    submitOn=models.DateField(blank=True)
    img =models.ImageField(verbose_name= 'Image 1',upload_to='static/images/listing_images',blank=True)
    img2 =models.ImageField(verbose_name= 'Image 2',upload_to='static/images/listing_images',blank=True,null=True)
    img3 =models.ImageField(verbose_name= 'Image 3',upload_to='static/images/listing_images',blank=True,null=True)
    isFeatured= models.BooleanField(default=False)
    user_id=models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    #properity owner details
    contact=models.CharField(max_length=256, blank=True, null=True)
    name=models.CharField(max_length=256, blank=True, null=True)
    #submitOn=models.DateField
    #def __str__(self):
        #return self.property_title
    def __str__(self):
         return "property_type"

    def getTopCitiesForRent():
        allCities=AgentCity.objects.all()
        citiesList=[]
        citiesList=allCities
        TopCityForRent={}
        for city in citiesList:
     #    get all cities id by parent loop
            city_id=city.id
            city_name=city.cityName
            countProperties=listing.objects.select_related('AgentCity_id').filter(AgentCity_id_id=city_id,purpose="Rent",property_type="House").prefetch_related('relatedCity').count()
            if countProperties != 0:
              TopCityForRent[city_name]=countProperties
        TopCityForRent=dict(sorted(TopCityForRent.items(),key=operator.itemgetter(1),reverse=True)) #geting dictionary in ascending order       
   
        return TopCityForRent
        
    def getTopCitiesForSale():
        allCities=AgentCity.objects.all()
        citiesList=[]
        citiesList=allCities
        TopCityForSale={}
        for city in citiesList:
     #    get all cities id by parent loop
            city_id=city.id
            city_name=city.cityName
            countSaleProperties=listing.objects.select_related('AgentCity_id').filter(AgentCity_id_id=city_id,purpose="Sale",property_type="House").prefetch_related('relatedCity').count()
            if countSaleProperties != 0:
              TopCityForSale[city_name]=countSaleProperties
        TopCityForSale=dict(sorted(TopCityForSale.items(),key=operator.itemgetter(1),reverse=True)) #geting dictionary in ascending order       
   
        return TopCityForSale
    def searchListing(City_id):#, type,status,beds,baths,minP,maxP
        lists=listing.objects.filter(AgentCity_id_id=City_id)
        dictionary={'lists':lists}

        return HttpResponse(dictionary) 
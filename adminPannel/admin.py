from importlib.resources import Package
from django.contrib import admin

from adminPannel.models import AdminSettings,homePage, package_services, services_offer, userOffer, userPackage,userService, Contact

class UserOfferAdmin(admin.ModelAdmin):
   list_display= ('name','duration', 'charges')
class userPackageList(admin.ModelAdmin):
   list_display=('package_name','desc','discount','prince')  
class packServiceList(admin.ModelAdmin):
   list_display=('duration','package_id','service_id')
class userServiceList(admin.ModelAdmin):
   list_display=('service_name', 'desc','charges')
class servicesOfferList(admin.ModelAdmin):
   list_display=('offer_id','service_id')   
   #Register your models here.


admin.site.register(userPackage,userPackageList)
admin.site.register(package_services,packServiceList)
admin.site.register(userService,userServiceList)
admin.site.register(userOffer, UserOfferAdmin)
admin.site.register(services_offer,servicesOfferList)
admin.site.register(Contact)
admin.site.register(AdminSettings)
admin.site.register(homePage)
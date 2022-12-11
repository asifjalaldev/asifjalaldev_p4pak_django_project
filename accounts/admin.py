from django.contrib import admin

from accounts.models import Profile
class profileList(admin.ModelAdmin):
    list_display= ('user', 'phone', 'isAgent', 'isFeatureAgent', 'website_url')
# Register your models here.
admin.site.register(Profile,profileList)
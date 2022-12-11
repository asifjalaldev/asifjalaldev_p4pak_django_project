
from typing import Set
from django.db import models

# Create your models here.
class userPackage(models.Model):
    package_name=models.CharField(max_length=50)
    desc=models.TextField(verbose_name='Description' ,blank=True)
    discount=models.DecimalField( max_digits=10, decimal_places=2)
    prince=models.DecimalField(max_digits=10, decimal_places=2)
class userService(models.Model):
    service_name=models.CharField(max_length=50)
    desc=models.TextField(blank=True)
    charges=models.DecimalField(max_digits=10, decimal_places=2)
class package_services(models.Model):
    duration=models.IntegerField()
    package_id=models.ForeignKey(userPackage, on_delete=models.SET_NULL,null=True)
    service_id=models.ForeignKey(userService, on_delete=models.SET_NULL, null=True)
class userOffer(models.Model):
    name=models.CharField(verbose_name='Offer Name', max_length=50)
    duration=models.IntegerField(verbose_name='Duration(Days)')
    charges=models.DecimalField(max_digits=10, decimal_places=2)
class services_offer(models.Model):
    offer_id=models.ForeignKey(userOffer, on_delete=models.SET_NULL,null=True)
    service_id=models.ForeignKey(userService, on_delete=models.SET_NULL, null=True)
class Contact(models.Model):
    officeAdress=models.CharField(verbose_name='office address', max_length=50)
    officeContact=models.CharField(verbose_name='Office Contact', max_length=120)
    officeMobile=models.CharField(verbose_name='Ofice Mobile', max_length=50)
    officeEmail=models.CharField(verbose_name='Email', max_length=50)
    WorkingHourse=models.CharField(verbose_name='working Hourse and Office Time', max_length=100)
class AdminSettings(models.Model):
    # homeSliderImage=models.ImageField(verbose_name='Home Image 1 (size: width=2000px, hight=1000)',blank=True, null=True)
    sideBanner=models.ImageField(verbose_name='sideBanner size(width=700px, height=1500px',blank=True, null=True)
    midBanner=models.ImageField(verbose_name='horizentalBanner size(width=750px, height=150px',blank=True, null=True)
class homePage(models.Model):
    homeSliderImage=models.ImageField(verbose_name='Home Image 1 (size: width=2000px, hight=1000)',blank=True, null=True)
    headerTextHeading=models.CharField(verbose_name='Heading', max_length=150,blank=True, null=True)
    # headerTextDescription=models.TextField(verbose_name='Description' ,blank=True)
    
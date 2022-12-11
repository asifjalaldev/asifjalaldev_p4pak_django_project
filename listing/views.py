from pyexpat.errors import messages
from django.shortcuts import redirect, render
from django.contrib import messages

from adminPannel.models import Contact
from .models import listing
from django.db.models import Q
from django.core.paginator import Paginator
from django.contrib.auth.models import User
from agentDirectory.models import AgentCity
import datetime
from django.utils.datastructures import MultiValueDictKeyError
from django.contrib.auth.decorators import login_required
# Create your views here.
def searchListing(request):
    contact=Contact.objects.all()
    # city_id=request.GET['city']
    type=request.GET['type']
    status=request.GET['status']
    beds=request.GET['bedrooms']
    baths=request.GET['bathrooms']
    minP=request.GET.get('minPrice')
    maxP=request.GET.get('maxPrice')
    city_id=request.GET['city']
    # page_obj=searchListing(city_id)
    page_obj=listing.objects.filter(AgentCity_id_id=city_id,property_type__icontains=type,purpose__icontains=status,bedroom__icontains=beds,bathroom__icontains=baths,rental_price__lte=maxP,rental_price__gte= minP)
    count=len(page_obj)
    context={'page_obj': page_obj,'count':count, 'contact':contact}
    return render(request, 'user/real-places-html/searchProperties.html',context)

def viewSingleList(request,pk):
    listDetail=listing.objects.get(id=pk)
    contact=Contact.objects.all()
    if(listDetail.user_id != None):
         user=User.objects.get(username=listDetail.user_id)
         context={'listDetail': listDetail,'user':user,'contact':contact}
         return render(request, 'user/real-places-html/property-single.html',context)
    else:
        contact=Contact.objects.all()
        context={'listDetail': listDetail,'contact':contact}
        return render(request, 'user/real-places-html/property-single.html',context)
@login_required(login_url='/accounts/nonStaffUserLogin/')
def myListing(request):
    listings=listing.objects.filter(user_id=request.user.id)
    contact=Contact.objects.all()
    paginator = Paginator(listings,4)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context={'listings':page_obj, 'contact':contact}
    return render(request, 'user/real-places-html/my-properties.html',context)
def boostProperty(request):
    return render(request, 'user/real-places-html/packages.html')
#edit listing
@login_required(login_url='/accounts/register/')
def editListing(request,pk):
    if pk!=0 and request.method=='GET':
        list=listing.objects.get(id=pk)
        # featured=list.isFeatured
        allCities=AgentCity.objects.all()
        city=AgentCity.objects.get(id=list.AgentCity_id.id)
        contact=Contact.objects.all()
        context={'list':list,'city':city,'allCities':allCities,'contact':contact}
        return render(request, 'user/real-places-html/editListing .html',context)
    if pk!=0 and request.method == 'POST':
            title=request.POST.get('title')
            purpose=request.POST.get('purpose')
            property_type=request.POST.get('type')
            cityID=request.POST.get('city')
            city=AgentCity.objects.get(id=cityID)
            Location=request.POST.get('location')
            desc=request.POST.get('description')
            rental_price=request.POST.get('price')
            land_area=request.POST.get('area')
            unit=request.POST.get('unit')
            bedroom=request.POST.get('bedroom')
            bathroom=request.POST.get('bathroom')
            Owner_name=request.POST.get('name')
            Owner_contact=request.POST.get('contact')
            isFeatured=request.POST.get('Feature')
            # isFeatured=featured
            # try:
            #     isFeatured=request.POST.get('featured',False)
            # except MultiValueDictKeyError:
            #     isFeatured = False
            submitOn=datetime.date.today()
            user_id= request.POST.get('userId')
            user=User.objects.get(id=user_id)
            
            img=request.FILES.get('img',False)
            # try:
            img2=request.FILES.get('img2',False)
            img3=request.FILES.get('img3',False)
            if img == False:
                old_img=request.POST.get('old_img')
                img=old_img

            # try:
            if img2==False:
                old_img2=request.POST.get('old_img2')
                img2=old_img2
            if img3==False:
              
                old_img3=request.POST.get('old_img3')
                img3=old_img3
            # except MultiValueDictKeyError:
                
            #     img2 = False
            #     img3 = False
            my_property=listing(id=pk,property_title=title, purpose=purpose, property_type=property_type,AgentCity_id=city , Location=Location, desc=desc
                , rental_price=rental_price, land_area=land_area,unit=unit, bedroom=bedroom, bathroom=bathroom,submitOn=submitOn, isFeatured=isFeatured,user_id=user,img=img,img2=img2,img3=img3
                 ,name=Owner_name, contact=Owner_contact)
                 
            my_property.save()
            messages.info(request,"Propertiy updated successfuly!")
            list=listing.objects.get(id=pk)
            allCities=AgentCity.objects.all()
            city=AgentCity.objects.get(id=list.AgentCity_id.id)
            context={'list':list,'city':city,'allCities':allCities}
            return render(request, 'user/real-places-html/editListing .html',context)
            # return render(request, 'user/real-places-html/my-properties.html',context)
    
#delete listing
@login_required(login_url='/accounts/register/')
def delelteListing(request,pk):
    if pk != 0:
        list=listing.objects.get(id=pk)
        list.delete()
        messages.info(request, "properity deleted successfully")
        listings=listing.objects.filter(user_id=request.user.id)

        context={'listings':listings}
        return render(request, 'user/real-places-html/my-properties.html',context)
    else:
        messages.info(request, "properity not found")
        listings=listing.objects.filter(user_id=request.user.id)
        context={'listings':listings}
        return render(request, 'user/real-places-html/my-properties.html',context)
@login_required(login_url='/accounts/register/')
def submitListing(request):
    if request.user.is_authenticated:
       city=AgentCity.objects.all()
       contact=Contact.objects.all()
       context={'city': city,'contact':contact}
    if request.user.is_authenticated and request.method=="POST":
        if request.user.is_authenticated:#if user is registered
            title=request.POST.get('title')
            purpose=request.POST.get('purpose')
            property_type=request.POST.get('type')
            cityID=request.POST.get('city')
            city=AgentCity.objects.get(id=cityID)
            Location=request.POST.get('location')
            desc=request.POST.get('description')
            rental_price=request.POST.get('price')
            land_area=request.POST.get('area')
            unit=request.POST.get('unit')
            bedroom=request.POST.get('bedroom')
            bathroom=request.POST.get('bathroom')
            try:
                isFeatured=request.POST.get('featured',False)
            except MultiValueDictKeyError:
                isFeatured = False
            submitOn=datetime.date.today()
            user_id= request.POST.get('userId')
            user=User.objects.get(id=user_id)
            img=request.FILES.get('img',False)
            img2=request.FILES.get('img2',False)
            img3=request.FILES.get('img3',False)
            Owner_name=request.POST.get('name')
            Owner_contact=request.POST.get('contact')
           
            # except MultiValueDictKeyError:
                
            #     img2 = False
            #     img3 = False
            my_property=listing(property_title=title, purpose=purpose, property_type=property_type,AgentCity_id=city , Location=Location, desc=desc
                , rental_price=rental_price, land_area=land_area,unit=unit, bedroom=bedroom, bathroom=bathroom,submitOn=submitOn, isFeatured=isFeatured,user_id=user,img=img,img2=img2,img3=img3
                  ,name=Owner_name,contact=Owner_contact)
                 
            my_property.save()
            messages.info(request,"Your Propertiy submited successfuly!")
            return render(request, 'user/real-places-html/submitListing.html',context)
    else:

        return render(request, 'user/real-places-html/submitListing.html',context)

  
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.shortcuts import redirect, render
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from listing.models import listing
from agentDirectory.models import AgentCity, AgentDir
import datetime
from django.contrib.auth.models import User
from django.utils.datastructures import MultiValueDictKeyError
from django.core.paginator import Paginator
# Create your views here.
def adminLogin(request):
    if request.method=='POST':
        username=request.POST['username']
        password=request.POST['password']
        user = authenticate( username=username , password=password)
        if user is not None and user.is_staff==True and user.is_active:
            login(request, user)
            #return redirect(request,'admin/admin_main.html')
            return render(request, 'admin/admin_main.html')
        else:
            messages.error(request,'incorect username or password')
            #return render(request,'admin/adminLogin.html')
            return redirect('adminLogin') 
    else:
        return render(request,'admin/adminLogin.html')
def logOut(request):
    if request.user.is_authenticated:
       logout(request)
       return redirect('adminLogin') 
@login_required(login_url='/adminPannel/adminLogin/')
def dashboard(request):
    if request.user.is_authenticated:
       #return redirect('dashboard')
       return render(request, 'admin/admin_main.html')
    else:
        return redirect('adminLogin') 
       #return render(request,'admin/adminLogin.html')
    #  return redirect('%s?next=%s' % (settings.LOGIN_URL, request.path))
@login_required(login_url='/adminPannel/adminLogin/')
def insertCityFromAddListing(request):
    if request.method=='POST' and request.POST.get('cityName')!="":
        cityName=request.POST.get('cityName')
        city=AgentCity(cityName=cityName)
        city.save()
        messages.info(request,"City submited successfuly!")
        city=AgentCity.objects.all()
        context={'city':city}
        return render(request, 'admin/AddListing.html',context)
# def searchCity(request):
#     if request.method =='get' and request.POST.get('searchCityName')!= 'None':
#         searchCityName=str(request.GET.get('searchCityName')).capitalize()
#         searchCity=AgentCity.objects.filter(cityName=searchCityName)
#         if searchCity is not None:
#             city=AgentCity.objects.all()
#             paginator = Paginator(city, 12) # Show 12 agents per page 
#             page_number = request.GET.get('page')
#             page_obj = paginator.get_page(page_number)
#             context={'city':page_obj, 'searchCity':searchCity}
#             return render(request, 'admin/city.html',context)
#         else:
#             city=AgentCity.objects.all()
#             paginator = Paginator(city, 12) # Show 12 agents per page 
#             page_number = request.GET.get('page')
#             page_obj = paginator.get_page(page_number)
#             messages.info(request, "Oops! City Not Found.")
#             context={'city':page_obj}
#             return render(request, 'admin/city.html',context)
#     city=AgentCity.objects.all()
#     paginator = Paginator(city, 12) # Show 12 agents per page 
#     page_number = request.GET.get('page')
#     page_obj = paginator.get_page(page_number)
#     messages.info(request, "Oops! City Not Found.")
#     context={'city':page_obj}
#     return render(request, 'admin/city.html',context)
def viewCity(request):
    if request.method=='POST' and request.POST.get('cityName')!="":
        cityName=str(request.POST.get('cityName')).capitalize()
        check=AgentCity.objects.get(cityName=cityName)
        if check is not None:
            messages.info(request,"Oops! city name" + cityName+" Already Exists")
            city=AgentCity.objects.all()
            paginator = Paginator(city, 12) # Show 12 agents per page 
            page_number = request.GET.get('page')
            page_obj = paginator.get_page(page_number)
            context={'city':page_obj}
            return render(request, 'admin/city.html',context)
        else:
            newCity=AgentCity(cityName=cityName)
            newCity.save()
            messages.info(request,"New City added successfuly!")
            city=AgentCity.objects.all()
            paginator = Paginator(city, 12) # Show 12 agents per page 
            page_number = request.GET.get('page')
            page_obj = paginator.get_page(page_number)
            context={'city':page_obj}
            return render(request, 'admin/city.html',context)
    else:
         city=AgentCity.objects.all()
         paginator = Paginator(city, 12) # Show 12 agents per page 
         page_number = request.GET.get('page')
         page_obj = paginator.get_page(page_number)
         context={'city':page_obj}
         return render(request, 'admin/city.html',context)

def viewAgentDir(request):
    dir=AgentDir.objects.all()
    agentsPaginator=Paginator(dir, 10)
    page_number = request.GET.get('page')
    agentsPaginator_obj = agentsPaginator.get_page(page_number)

    context={'agentsPaginator_obj':agentsPaginator_obj}
    return render(request,'admin/agentDir.html',context)
@login_required(login_url='/adminPannel/adminLogin/')
def addListing(request):
    if request.user.is_authenticated:
       city=AgentCity.objects.all()
       context={'city': city}
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
            user_id= request.user.id
            user=User.objects.get(id=user_id)

            img=request.FILES['img']
            img2=request.FILES.get('img2',False)
            img3=request.FILES.get('img3',False)
            name=request.POST.get('name')
            contact=request.POST.get('contact')
            my_property=listing(property_title=title, purpose=purpose, property_type=property_type,AgentCity_id=city , Location=Location, desc=desc
            , rental_price=rental_price, land_area=land_area,unit=unit, bedroom=bedroom, bathroom=bathroom,submitOn=submitOn, isFeatured=isFeatured,user_id=user,img=img,img2=img2,img3=img3,
            contact=contact, name=name)
            my_property.save()
            messages.info(request,"Your Propertiy submited successfuly!")

            #return render(request, 'user/real-places-html/my-properties.html')
            return render(request, 'admin/AddListing.html',context)
        #if user is not registered!
        #else:
            #redirect to registeration page
    else:

        return render(request, 'admin/AddListing.html',context)


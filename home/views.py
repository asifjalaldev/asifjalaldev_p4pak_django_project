

from collections import UserDict
from json import dumps
from unicodedata import name
from adminPannel.models import Contact, homePage
from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
from adminPannel.models import userPackage
from agentDirectory.models import AgentCity, AgentDir, batch
from django.core.paginator import Paginator
from adminPannel.models import AdminSettings
from listing.models import listing
from django.contrib.auth.models import User
from accounts.models import Profile
import operator
# Create your views here.

def contact(request):
    contact=Contact.objects.all()
    context={'contact': contact}
    return render(request, 'user/real-places-html/contact.html',context)

def viewHome(request):
    #package_service = package_services.objects.get(package_id=1)
    # packages=userPackage.objects.all()
    # AgentDirectories=AgentDir.objects.all()
    listings=listing.objects.filter(isFeatured='True')
    contact=Contact.objects.all()
    agentCity=AgentCity.objects.all()
    header=homePage.objects.all()
    sideBanner=AdminSettings.objects.get()
    midBanner=AdminSettings.objects.get()
    platinumBadge=batch.objects.get(batch_name='Platinum')
    platinumAgent=AgentDir.objects.select_related('batch_id').filter(batch_id_id=platinumBadge.id)#use select_related to get the platinum agents only 
    paginator = Paginator(listings, 4) # Show 4 listings per page 
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    # get top cities for houses
    topSaleCities=listing.getTopCitiesForSale()
    topRentCities=listing.getTopCitiesForRent()
    topAgents=AgentDir.getTopAgents()
    users=User.objects.all()
    PlatinumAgentList=[]
    for user in users:
        if user.profile.isPlatinum==True:
            PlatinumAgentList.append(user)
    context={'users':users,'PlatinumAgentList':PlatinumAgentList,'TopCityForRent':topRentCities,'TopAgentDict':topAgents, 'TopcitiesForPropertyDict':topSaleCities ,'page_obj':page_obj,'agentsPaginator_obj':platinumAgent,'agentCity':agentCity, 'contact':contact,'header':header,'sideBanner':sideBanner,'midBanner':midBanner}
    return render(request, 'user/real-places-html/index.html', context)
    #listing django session tutoral in youtube Link: https://youtu.be/byt0geO8WDw 
def popularCityPropertyForSale(request,cityName):
    city_id=AgentCity.objects.get(cityName=cityName)
    listings=listing.objects.filter(purpose='Sale',AgentCity_id=city_id)
    contact=Contact.objects.all()
    paginator = Paginator(listings,24)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context={'page_obj': page_obj,'contact':contact}
    return render(request,'user/real-places-html/gallery-4-columns.html',context)
def popularCityPropertyForRent(request,cityName):
    city_id=AgentCity.objects.get(cityName=cityName)
    listings=listing.objects.filter(purpose='Rent',AgentCity_id=city_id)
    contact=Contact.objects.all()
    paginator = Paginator(listings,24)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context={'page_obj': page_obj,'contact':contact}
    return render(request,'user/real-places-html/gallery-4-columns.html',context)
def popularCityAgents(request,cityName):
    contact=Contact.objects.all()
    agentCity=AgentCity.objects.all()
    city_id=AgentCity.objects.get(cityName=cityName)
    cityAgents=AgentDir.objects.filter(AgentCity_id_id=city_id)
    paginator = Paginator(cityAgents, 12) # Show 12 agents per page 
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context={'page_obj':page_obj, 'agentCity':agentCity,'contact':contact,'agents':cityAgents  }
    return render(request,'user/real-places-html/Agents-3-col.html',context)
def viewAgents(request):
    agents=AgentDir.objects.all()
    agentCity=AgentCity.objects.all()
    contact=Contact.objects.all()
    paginator = Paginator(agents, 12) # Show 12 agents per page 
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context={'page_obj':page_obj, 'agentCity':agentCity,'contact':contact,'agents':agents  }
    return render(request,'user/real-places-html/agents.html',context)
    
    #search code
def searchAgent(request):
    requiredCityID=request.GET.get('city_id')
    agentName=request.GET.get('search_name')
    agents=AgentDir.objects.filter(AgentCity_id_id=requiredCityID,name__icontains=agentName)
    agentCity=AgentCity.objects.all()
    contact=Contact.objects.all()
    paginator = Paginator(agents, 2) # Show 12 agents per page 
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    get_copy = request.GET.copy()
    parameters = get_copy.pop('page', True) and get_copy.urlencode()
    context={'page_obj':page_obj, 'agentCity':agentCity, 'contact':contact,'agents':agents,'parameters':parameters }
    return render(request,'user/real-places-html/Agents-3-col.html',context)
     
def viewListings(request):
    listings=listing.objects.all()
    paginator = Paginator(listings,24)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    contact=Contact.objects.all()
    context={'page_obj': page_obj, 'contact': contact}
    return render(request,'user/real-places-html/gallery-4-columns.html',context)

def forRent(request):
    listings=listing.objects.filter(purpose='Rent')
    contact=Contact.objects.all()
    paginator = Paginator(listings,24)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context={'page_obj': page_obj,'contact':contact}
    return render(request,'user/real-places-html/gallery-4-columns.html',context)

def forSale(request):
    listings=listing.objects.filter(purpose='Sale')
    contact=Contact.objects.all()
    paginator = Paginator(listings,24)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context={'page_obj': page_obj,'contact':contact}
    return render(request,'user/real-places-html/gallery-4-columns.html',context)
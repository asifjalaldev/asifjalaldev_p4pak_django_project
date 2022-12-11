from unicodedata import name
from django.urls import path,include
from . import views
urlpatterns = [
    path('',views.viewHome, name='viewHome'),
    path('viewAgents', views.viewAgents, name='viewAgents'),

    path('searchAgent', views.searchAgent, name='searchAgent'),
    path('viewListings',views.viewListings, name='viewListings'),
    path('forSale', views.forSale, name='forSale'),
    path('forRent', views.forRent, name='forRent'),
    path('contact',views.contact, name='contact'),
    path('popularCityAgents/<str:cityName>/',views.popularCityAgents,name='popularCityAgents'),
    path('popularCityPropertyForRent/<str:cityName>/',views.popularCityPropertyForRent,name='popularCityPropertyForRent'),
    path('popularCityPropertyForSale/<str:cityName>/',views.popularCityPropertyForSale,name='popularCityPropertyForSale')

]
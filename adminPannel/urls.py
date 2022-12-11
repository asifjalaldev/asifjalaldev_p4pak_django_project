from django.urls import path,include
from . import views
urlpatterns = [
    path('',views.dashboard, name='dashboard'),
    path('adminLogin/',views.adminLogin,name='adminLogin'),
    path('logOut/',views.logOut,name='logOut'),
    path('addListing/',views.addListing, name='addListing'),
    path('viewCity/',views.viewCity, name='viewCity'),
    path('viewAgentDir/',views.viewAgentDir, name='viewAgentDir'),
    # path('searchCity/',views.searchCity, name='searchCity'),
    path('insertCityFromAddListing/',views.insertCityFromAddListing, name='insertCityFromAddListing')
]

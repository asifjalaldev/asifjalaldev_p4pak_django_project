from django.urls import path,include
from . import views
urlpatterns = [
    path('myListing/',views.myListing,name='myListing'),
      path('submitListing/',views.submitListing,name='submitListing'),
      path('viewSingleList/<int:pk>/',views.viewSingleList, name='viewSingleList'),
      path('delelteListing/<int:pk>/',views.delelteListing,name='delelteListing'),
       path('editListing/<int:pk>/',views.editListing,name='editListing'),
       path('boostProperty',views.boostProperty,name='boostProperty'),
      path('searchListing', views.searchListing, name='searchListing')
]

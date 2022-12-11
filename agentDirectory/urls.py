from django.urls import path,include
from . import views
urlpatterns = [
    path('',views.ShowAgentDir, name='ShowAgentDir'),
    path('searchAgents', views.searchAgents, name='searchAgents'),
    path('editAgent/<int:pk>/',views.editAgent,name='editAgent'),
    path('agentDetails/<int:pk>/',views.agentDetails,name='agentDetails')
]

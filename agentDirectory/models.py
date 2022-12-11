from operator import truediv
import operator
from django.db import models
from django.forms import IntegerField

from accounts.queryDebugger import query_debugger
# Create your models here.

class AgentCity(models.Model):
    cityName=models.CharField(max_length=50)
class batch(models.Model):
     batch_name=models.CharField(max_length=230)
class AgentDir(models.Model):
    name=models.CharField(max_length=230)
    phoneNo=models.CharField(verbose_name='Phone Number' ,max_length=256, blank=True, null=True)
    img=models.ImageField(verbose_name='Image', blank=True, null=True)
    address=models.CharField(max_length=250, blank=True, null=True)
    AgentCity_id=models.ForeignKey(AgentCity, related_name='relatedAgentCity' , on_delete=models.SET_NULL,null=True)
    status=models.CharField(max_length=50, blank=True, null=True,default=False)
    batch_id=models.ForeignKey(batch,related_name='relatedBadge', on_delete=models.SET_NULL,null=True,blank=True)
    facebook_url=models.CharField(max_length=250,blank=True,null=True)
    email_address=models.CharField(max_length=250,blank=True,null=True)
    website_address=models.CharField(max_length=250,blank=True,null=True)
    isFeatured= models.BooleanField(default=False)
 
    def getTopAgents():
        allCities=AgentCity.objects.all()
        citiesList=[]
        citiesList=allCities
        TopAgentDict={}
        for city in citiesList:
     #    get all cities id by parent loop
            city_id=city.id
            city_name=city.cityName
            countAgents=AgentDir.objects.select_related('AgentCity_id').filter(AgentCity_id_id=city_id).count()
            if countAgents !=0:
                TopAgentDict[city_name]=countAgents
        TopAgentDict=dict(sorted(TopAgentDict.items(),key=operator.itemgetter(1),reverse=True))#sort agentDict in ascending order by value
        return TopAgentDict
import operator
from django.db import models

from agentDirectory.models import AgentDir

# Create your models here.

def getTopAgents():
    citiesList=[]
    TopAgentDict={}
    for city in citiesList:
     #    get all cities id by parent loop
        city_id=city.id
        city_name=city.cityName
        countAgents=AgentDir.objects.filter(AgentCity_id_id=city_id).count()
        if countAgents !=0:
            TopAgentDict[city_name]=countAgents
    TopAgentDict=dict(sorted(TopAgentDict.items(),key=operator.itemgetter(1),reverse=True))#sort agentDict in ascending order by value
    return TopAgentDict

        
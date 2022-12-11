
from django.shortcuts import render

from django.contrib import messages

from agentDirectory.models import AgentCity, AgentDir, batch
from django.utils.datastructures import MultiValueDictKeyError
# Create your views here.
def ShowAgentDir(request):
    pass
def searchAgents(request):
    if request.method == 'GET':
        agentName=request.GET.get('agent_name')
        featured=request.GET.get('isFeatured')
        
        if agentName=="" and featured=='True':
            FeatureAgents=AgentDir.objects.filter(isFeatured=featured)
            context= {'agentsPaginator_obj':FeatureAgents}
            return render(request, 'admin/agentDir.html',context)
        elif agentName !="" and featured == 'False':
            
            agent= AgentDir.objects.filter(name__icontains=agentName)
        
            context= {'agentsPaginator_obj':agent}
     
            return render(request, 'admin/agentDir.html',context)
        elif  agentName == "" and featured == 'platinum':
            badg=batch.objects.get(batch_name='Platinum')
            badgId=badg.id
            agent= AgentDir.objects.select_related('batch_id').filter(batch_id_id=badgId)
        
            context= {'agentsPaginator_obj':agent}
     
            return render(request, 'admin/agentDir.html',context)
    else:
        print(agentName)
        messages.info(request,"no agent found")
        return render(request, 'admin/agentDir.html')
def agentDetails(request, pk):
        agent= AgentDir.objects.get(id=pk)
        context={'agent':agent}
        return render(request,'user/real-places-html/agent-single.html',context)
     
def editAgent(request, pk):
    if request.method=='GET':
        allCities=AgentCity.objects.all()
        agent= AgentDir.objects.get(id=pk)
        badges=batch.objects.all()
        # city=AgentCity.objects.get(id=agent.Agentcity_id.id)
        context={'agent': agent,'allCities':allCities, 'badges':badges}
        return render(request, 'admin/editAgent.html',context)
    elif pk!=0 and request.method == 'POST':
        name=request.POST.get('name')
        phoneNo=request.POST.get('phoneNo')
        address=request.POST.get('address')
        website_address=request.POST.get('website_address')
        status=request.POST.get('status')
        email=request.POST.get('email')
        cityID=request.POST.get('city')
        city=AgentCity.objects.get(id=cityID)
        try:
            isFeatured=request.POST.get('isFeatured')
        except MultiValueDictKeyError:
            isFeatured = False

        img=request.FILES.get('img',False)
        badge_id=request.POST.get('badge')
       #correct this code
        if badge_id !='0':
          badges=batch.objects.get(id=badge_id)
        if img == False:
                old_img=request.POST.get('old_img')
                img=old_img
        if badge_id =='0':
            agent=AgentDir(id=pk, name=name, phoneNo=phoneNo,address=address,AgentCity_id=city,status=status,
             email_address=email,website_address=website_address,isFeatured=isFeatured,img=img)
        else:
            agent=AgentDir(id=pk, name=name, phoneNo=phoneNo,address=address,AgentCity_id=city,status=status,
            email_address=email,website_address=website_address,isFeatured=isFeatured,batch_id=badges,img=img)
        agent.save()
        allCities=AgentCity.objects.all()
        agent= AgentDir.objects.get(id=pk)
        badges=batch.objects.all()
        # city=AgentCity.objects.get(id=agent.Agentcity_id.id)
        messages.info(request,"agent updated successfully")
        context={'agent': agent,'allCities':allCities, 'badges':badges}
        return render(request, 'admin/editAgent.html',context)
    else:
       
        messages.info(request,"no agent found")
        return render(request, 'admin/editAgent.html')

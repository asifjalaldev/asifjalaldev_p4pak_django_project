from django.contrib import messages
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import redirect, render
from django.contrib import auth
from accounts.models import Profile
from agentDirectory.models import AgentCity
from listing.models import listing
#from accounts.forms import RegisterForm
from .forms import RegisterForm
from django.contrib.auth.models import User
# Create your views here.
#new user registeration function
def register(response):
    if response.method == "POST":
        form = RegisterForm(response.POST)
        if form.is_valid():
            form.save()
            
            username = form['username'].value()
            user=User.objects.get(username=username)
            auth.login(response, user)
            next_url = response.GET.get('next')
            if next_url:
                return HttpResponseRedirect(next_url)
            else:
                return redirect("/")
        else:
            messages.info(response, "ooOps! invalid input.")
            return render(response, "user/real-places-html/registerUser.html", {"form":form})
    else:
        form = RegisterForm()

        return render(response, "user/real-places-html/registerUser.html", {"form":form})
# end register New     this is comment
# def registerUser(request): 
#     form = CustomUserCreationForm(request.POST) 
#     if form.is_valid(): 
#             form.save() 
#             username = form.cleaned_data.get('username') 
#             password = form.cleaned_data.get('password1') 
#             password = form.cleaned_data.get('password2') 
#             user = authenticate(request, username=username, password=password) 
#             login(request, user) 
#             return redirect('/') 
#     else:
#         messages.error(request, "Your data is not valid ")
#         return redirect('/')
#   login user are as following!!! 
def nonStaffUserLogin(request):

    if request.method=='POST':
        user_username=request.POST.get('username')
        user_password=request.POST.get('password')
        user = auth.authenticate(request, username=user_username, password=user_password)
        if user is not None:
            auth.login(request, user)
            messages.info(request, f"You are now logged in as {user_username}")
            request.session['user_username']=user.username
            request.session['user_email']=user.email
           
            return redirect("/")
    # A backend authenticated the credentials
        else:
    # No backend authenticated the credentials
            messages.error(request, "incorect username or password ")
            return render(request,'user/real-places-html/user_login.html')
    else:
        return render(request,'user/real-places-html/user_login.html')
def userLogout(request):
    auth.logout(request)
    messages.success(request, 'Logout successfully!')
    return redirect('/')
def viewProfile(request):
    currentUser=request.user
    userProfile=Profile.objects.get(user=currentUser)
    user=User.objects.get(id=currentUser.id)
    # userProfile=Profile.objects.get(user.id=currentUser.id)
    # userProfileDetails=UserProfile.objects.get(id=currentUser.id) 
    context={'userProfile':userProfile}
    return render(request,"user/real-places-html/viewProfile.html",context)
def editProfile(request,pk):
    # code for creating profile of all existing users
    # user=User.objects.filter(profile=None)
    # for user in user:
    #     Profile.objects.create(user=user)
    #     print("user profile Created")
    if request.method == 'GET':
        # user=User.objects.get(id=pk)
        userProfile=Profile.objects.get(id=pk)
        allCities=AgentCity.objects.all()
        if userProfile.AgentCity_id_id is not None:
            city1=AgentCity.objects.get(id=userProfile.AgentCity_id_id)
            context={'city1':city1,'userProfile':userProfile,'allCities':allCities}
        else:
            context={'userProfile':userProfile,'allCities':allCities}
        return render(request,"user/real-places-html/EditProfile.html",context)
    if request.method == 'POST':
        profilePhoto=request.FILES.get('img',False)
        bio=request.POST.get('description')
        cityID=request.POST.get('city')
        if cityID:
            city=AgentCity.objects.get(id=cityID)
# self awareness 
# 1 - see what gives results . that is your strength. 
# 2- feedback of people's define 
# 3- your thougth
# 4- reflect
        fullName=request.POST.get('name')
        # type=request.GET['email']
        phone=request.POST.get('phonNumber')
        inst=request.POST.get('instagram-url')
        fb=request.POST.get('facebook-url')
        twit=request.POST.get('twitter-url')
        web=request.POST.get('website-url')
        address=request.POST.get('address')
        if profilePhoto == False:
                old_img=request.POST.get('old_img')
                profilePhoto=old_img
        agentProfile=Profile(user=request.user,id=pk, bio=bio,AgentCity_id=city, phone=phone,
        fullName=fullName,address=address,profilePhoto=profilePhoto,
        website_url=web,facebook_url=fb, twitter_url=twit, instagram_url=inst)
        agentProfile.save()
        userProfile=Profile.objects.get(id=pk)
        print(userProfile.AgentCity_id_id)
        # if userProfile.AgentCity_id_id != None:this is comment 
        city1=AgentCity.objects.get(id=userProfile.AgentCity_id_id)

        allCities=AgentCity.objects.all()
        context={'city1':city1,'userProfile':userProfile,'allCities':allCities}
        messages.info(request,"Profile updated successfuly!")
        
        return render(request,"user/real-places-html/EditProfile.html",context)
def RegisteredAgentDetails(request,pk):
    if pk != 0:
        userProfile=Profile.objects.get(user_id=pk)
        userProperties=listing.objects.filter(user_id=pk)
        context={'userProfile':userProfile,'userProperties':userProperties}
    return render(request, "user/real-places-html/RegisterAgentProfile.html",context)
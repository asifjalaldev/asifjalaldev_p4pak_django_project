
import datetime
from django.db import models
from django.contrib.auth.models import User
from django.utils.timezone import now
from agentDirectory.models import AgentCity, batch
from django.dispatch import receiver #add this
from django.db.models.signals import post_save #add this
# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    AgentCity_id=models.ForeignKey(AgentCity, related_name='relatedRegisteredAgentCity' , on_delete=models.SET_NULL,null=True)
    bio=models.TextField(verbose_name='bio' ,blank=True)
    phone = models.CharField(max_length=256, blank=True, null=True)
    fullName=models.CharField(max_length=130, blank=True)
    address=models.CharField(max_length=230, blank=True)
    profilePhoto= models.ImageField(verbose_name='profilePhoto size(width=220px, height=220px)',blank=True, null=True)
    isAgent=models.BooleanField(default=False)
    joiningDate=models.DateField(default=now, blank=True)
    isGold=models.BooleanField(default=False)
    isPlatinum=models.BooleanField(default=False)
    website_url=models.CharField(max_length=250, blank= True)
    facebook_url=models.CharField(max_length=250, blank= True)
    twitter_url=models.CharField(max_length=250, blank= True)
    instagram_url=models.CharField(max_length=250, blank= True)
    isFeatureAgent=models.BooleanField(default=False)
    def __str__(self):
        return str(self.user)  
    @receiver(post_save, sender=User)
    def create_profile(sender, instance, created, **kwargs):
        """Create a matching profile whenever a User is created."""
        if created:
            profile, new = Profile.objects.get_or_create(user=instance)
User.profile = property(lambda u: Profile.objects.get_or_create(user=u)[0])
  
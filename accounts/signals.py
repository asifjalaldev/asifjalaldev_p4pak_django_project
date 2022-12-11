from django.dispatch import receiver
from django.db.models.signals import pre_save, post_save
from .models import User, Profile


# @receiver(post_save, sender=User, dispatch_uid='user.create_user_profile')
# def create_user_profile(sender, instance, created, **kwargs):
#     if created:
#         Profile.objects.create(user=instance)


# @receiver(post_save, sender=User, dispatch_uid='user.save_user_profile')
# def save_user_profile(sender, instance, **kwargs):
#     instance.profile.save()
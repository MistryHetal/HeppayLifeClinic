# Purpose of this file is to make profile for each new user
from django.core.exceptions import ObjectDoesNotExist
from django.db.models.signals import post_save
from django.contrib.auth.models import User
from django.dispatch import receiver
from .models import Profile

# Receiver to recevie post_save signal when new user is created 
# @receiver(post_save, sender=User)
# def create_profile(sender, instance, created, **kwargs):
#     if created:
#         Profile.objects.create(user=instance)

# @receiver(post_save, sender=User)
# def save_profile(sender, instance, **kwargs):
#     try:
#         instance.profile.save()
#     except ObjectDoesNotExist:
#         Profile.objects.create(user=instance)

# @receiver(post_save, sender=User)
# def create_appointment(sender, instance, created, **kwargs):
#     if created:
#         Appointment.objects.create(user=instance)

# @receiver(post_save, sender=User)
# def save_appointment(sender, instance, **kwargs):
#     try:
#         instance.appointment.save()
#     except ObjectDoesNotExist:
#         Appointment.objects.create(user=instance)

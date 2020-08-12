from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

class College(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    email = models.TextField(max_length=500, blank=True)
    password = models.CharField(max_length=30, blank=True)
@receiver(post_save, sender=User)
def update_user_profile(sender, instance, created, **kwargs):
    if created:
        College.objects.create(user=instance)
    #instance.COLLEGENAME.save()

from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    username = models.CharField(max_length=64)
    email = models.CharField(max_length=64)
    first_name = models.CharField(max_length = 32)
    last_name = models.CharField(max_length = 32)
    phone_number = models.BigIntegerField(null=True)
    account_balance = models.BigIntegerField(null=True)

@receiver(post_save, sender=User)
def update_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)
    instance.profile.save()
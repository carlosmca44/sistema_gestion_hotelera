from django.contrib.auth import get_user_model
from django.db.models.signals import post_save
from .models import UserProfile
from django.dispatch import receiver


@receiver(post_save, sender=get_user_model())
def newUser(sender, instance, created, **kwargs):
    if created:
        UserProfile.objects.create(
            username=instance,
            first_name=instance.first_name,
            last_name=instance.last_name,
            password=instance.password,)

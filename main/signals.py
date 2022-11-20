from django.db.models.signals import post_save
from django.contrib.auth.models import User
from .models import Usuario
from django.dispatch import receiver


@receiver(post_save, sender=User)
def newUser(sender, instance, created, **kwargs):
    if created:
        Usuario.objects.create(
            username=instance,
            first_name=instance.first_name,
            last_name=instance.last_name,
            password=instance.password)

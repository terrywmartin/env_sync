from django.db.models.signals import post_save
from django.dispatch import receiver

from django.conf import settings
from .models import UserSettings ,User

def create_update_user_settings(sender, instance, created, **kwargs):
    if created:
        user = instance
        user = UserSettings.objects.create(user = user)


post_save.connect(create_update_user_settings, sender=User)





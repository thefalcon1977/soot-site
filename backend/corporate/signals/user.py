"""
Signal receivers for the User model.

This module contains signal receivers that are triggered by the User model's
`post_save` signal. These receivers handle the creation and update of the
related Profile model and the generation of referral codes for new users.
"""

from django.contrib.auth import get_user_model
from django.dispatch import receiver
from django.db.models.signals import post_save

from corporate.models import Profile


User = get_user_model()

@receiver(post_save, sender=User)
def save_or_update_profile(sender, instance, created, **kwargs):
    """
    Create or update the related Profile instance when a User is created or updated.

    :param sender: The User model class that sent the signal.
    :param instance: The User instance being saved.
    :param created: A boolean indicating whether the User instance was just created.
    :param kwargs: Additional keyword arguments.
    """
    Profile.objects.update_or_create(user=instance)
    instance.profile.save()

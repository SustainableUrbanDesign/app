from django.db.models.signals import post_save
from django.dispatch import receiver

from .models import User, UserProfile

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    """
    Create a profile for new user accounts (only when first saving the user).
    """
    print("Signal received")
    if created:
        user_profile = UserProfile(user=instance)
        
        user_profile.save()

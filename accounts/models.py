from django.db import models
from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

class Profile(models.Model):
    """
    This model extends the default Django User model.
    We DON'T need user_type field anymore because we'll use Django's is_staff/is_superuser
    """
    
    # One-to-one relationship with Django's built-in User model
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    
    # Additional profile fields (optional)
    phone = models.CharField(max_length=15, blank=True, null=True)
    address = models.TextField(blank=True, null=True)
    date_of_birth = models.DateField(null=True, blank=True)
    
    # Auto timestamps
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return f"{self.user.username}"
    
    @property
    def is_admin(self):
        """Check if user is admin (staff or superuser)"""
        return self.user.is_staff or self.user.is_superuser
    
    @property
    def is_client(self):
        """Check if user is client (not staff)"""
        return not self.user.is_staff

# SIGNALS: Automatically create Profile when User is created
@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    """
    This function runs automatically after a User is saved.
    If a new user is created, it creates a Profile for them.
    """
    if created:
        Profile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    """
    This function saves the profile whenever the user is saved.
    """
    if hasattr(instance, 'profile'):
        instance.profile.save()
# Create your models here.

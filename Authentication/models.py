from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver


class Profile(models.Model):

    GENDER_CHOICES = [
        ('Male', 'Male'),
        ('Female', 'Female'),
        ('Other', 'Other'),
    ]

    # Connect Profile to Django's built-in User
    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE
    )

    # Personal Information
    phone = models.CharField(
        max_length=15,
        blank=True,
        null=True
    )

    address = models.TextField(
        blank=True,
        null=True
    )

    date_of_birth = models.DateField(
        blank=True,
        null=True
    )

    gender = models.CharField(
        max_length=10,
        choices=GENDER_CHOICES,
        blank=True,
        null=True
    )

    # Health Information
    height = models.FloatField(
        blank=True,
        null=True,
        help_text="Height in cm"
    )

    current_weight = models.FloatField(
        blank=True,
        null=True,
        help_text="Current weight in kg"
    )

    fitness_goal = models.TextField(
        
        blank=True,
        null=True
    )

    allergies = models.TextField(
        blank=True,
        null=True,
        help_text="Food allergies or dietary restrictions"
    )

    # Dates
    created_at = models.DateTimeField(
        auto_now_add=True
    )

    updated_at = models.DateTimeField(
        auto_now=True
    )

    def __str__(self):
        return self.user.username

    @property
    def is_admin(self):
        return (
            self.user.is_staff
            or self.user.is_superuser
        )

    @property
    def is_client(self):
        return not self.user.is_staff

    #this is a property that checks if all required fields are filled out in the profile
    @property
    def records_completed(self):
        required_fields = [
            self.user.first_name,
            self.user.last_name,
            self.phone,
            self.gender,
            self.height,
            self.current_weight,
            self.fitness_goal,
        ]

        return all(required_fields)


# ==========================================
# AUTOMATICALLY CREATE PROFILE
# ==========================================

@receiver(post_save, sender=User)
def create_user_profile(
    sender,
    instance,
    created,
    **kwargs
):

    if created:
        Profile.objects.create(
            user=instance
        )


# ==========================================
# AUTOMATICALLY SAVE PROFILE
# ==========================================

@receiver(post_save, sender=User)
def save_user_profile(
    sender,
    instance,
    **kwargs
):

    if hasattr(instance, 'profile'):
        instance.profile.save()
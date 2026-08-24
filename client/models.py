#from django.db import models

# Create your models here.

'''from django.db import models
from django.contrib.auth.models import User

class Client(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone = models.CharField(max_length=15)
    date_of_birth = models.DateField(null=True, blank=True)
    address = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return f"{self.user.first_name} {self.user.last_name}"
    
    class Meta:
        db_table = 'clients'
        ordering = ['-created_at']'''

from django.db import models
from django.contrib.auth.models import User


class Client(models.Model):
    client_id = models.AutoField(primary_key=True)

    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE
    )

    phone = models.CharField(max_length=15)
    age = models.IntegerField()
    gender = models.CharField(max_length=20)
    height = models.FloatField()
    weight = models.FloatField()
    goal = models.CharField(max_length=255)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.user.username

    class Meta:
        db_table = 'clients'
        ordering = ['-created_at']
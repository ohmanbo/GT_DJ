from django.db import models
#from django.contrib.auth import get_user_model
from django.contrib.auth.models import AbstractUser

class account(AbstractUser):
    premium_account = models.BooleanField(default=False)
    profile_image = models.ImageField(default=None, blank=True)
    

class HelloWorld(models.Model):
    text = models.CharField(max_length=255, null=False)
 

# Create your models here.
class grid(models.Model):
    cell_id = models.IntegerField()
    cell_value = models.BinaryField()
    
class nearding(models.Model):
    cell_id = models.IntegerField()


    
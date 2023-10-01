from django.db import models
from django.db.models.functions import Lower

from users.models import User
from apikeys.models import APIKey
import uuid

# Create your models here.
class ConfigFile(models.Model):
    id = models.UUIDField(primary_key=True,unique=True,editable=False,default=uuid.uuid4)
    name = models.CharField(max_length=100,null=False,blank=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    user = models.ForeignKey(User,on_delete=models.CASCADE,null=True,blank=True)
    api_key = models.ForeignKey(APIKey, on_delete=models.SET_NULL, null=True, blank=True)
    def __str__(self):
        return self.name


class Location(models.Model):
    id = models.UUIDField(primary_key=True,unique=True,editable=False,default=uuid.uuid4)
    name = models.CharField(max_length=100,null=False,blank=False)
    user = models.ForeignKey(User,on_delete=models.CASCADE,null=True,blank=False)

    class Meta:
        ordering = [ Lower('name') ]

    def __str__(self):
        return self.name
    
class File(models.Model):
    id = models.UUIDField(primary_key=True,unique=True,editable=False,default=uuid.uuid4)
    name = models.CharField(max_length=100,null=False,blank=False)
    path = models.CharField(max_length=250, null=False,blank=False)
    environment = models.CharField(max_length=20,null=True,blank=True)
    s3_bucket = models.TextField(null=True,blank=True)

    config = models.ForeignKey(ConfigFile,on_delete=models.CASCADE,null=True,blank=True)
    location = models.ForeignKey(Location, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.name
    

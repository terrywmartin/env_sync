from django.db import models

from users.models import User

import uuid

# Create your models here.
class APIKey(models.Model):
    id = models.UUIDField(primary_key=True,unique=True,editable=False,default=uuid.uuid4)
    name = models.CharField(max_length=50,null=False,blank=False)
    hash = models.TextField(null=False,blank=False)
    prefix = models.CharField(max_length=10,null=False,blank=False)

    user = models.ForeignKey(User,on_delete=models.CASCADE,null=True,blank=True)

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
    

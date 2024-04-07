from django.db import models
from django.contrib.auth.models import AbstractUser
import uuid
# Create your models here.

class Users(AbstractUser):
    
    id=models.UUIDField(primary_key=True,default=uuid.uuid4,editable=False)
    musician=models.BooleanField(default=False)
    profile=models.ImageField(upload_to='Profile',null=True)
    
    REQUIRED_FIELDS=[]
    
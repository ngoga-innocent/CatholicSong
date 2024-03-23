from django.db import models
import uuid
from Accounts.models import Users
# Create your models here.

class SongType(models.Model):
    id=models.UUIDField(primary_key=True,default=uuid.uuid4,editable=False)
    name=models.CharField(max_length=255,null=False)
    season=models.CharField(max_length=255,null=True,default='Ibihe Bisanzwe')
    thumbnail=models.ImageField(upload_to='Song_Type',null=True)

    def __str__(self):
        return self.name
    
class Copies(models.Model):
    id=models.UUIDField(primary_key=True,default=uuid.uuid4,editable=False)
    name=models.CharField(max_length=255,null=False)
    composer=models.CharField(max_length=255,null=False)
    part=models.CharField(max_length=255,default="Other")
    uploader=models.ForeignKey(Users,on_delete=models.CASCADE,null=True)
    document=models.FileField(upload_to='songs_docs')
    category=models.ForeignKey(SongType,on_delete=models.CASCADE,null=True,default='')
    def __str__(self):
        return self.name


from django.db import models
import uuid
from Accounts.models import Users
import os
# Create your models here.

class SongType(models.Model):
    id=models.UUIDField(primary_key=True,default=uuid.uuid4,editable=False)
    name=models.CharField(max_length=255,null=False)
    season=models.CharField(max_length=255,null=True,default='Ibihe Bisanzwe')
    thumbnail=models.ImageField(upload_to='Song_Type',null=True)

    def __str__(self):
        return self.name
class SongCategory(models.Model):
    id=models.UUIDField(primary_key=True,default=uuid.uuid4,editable=False)
    name=models.CharField(max_length=255,null=False,default='Others',unique=True)
    def __str__(self):
        return self.name
def song_upload_path(instance, filename):
    # Get the category name
    category_name = instance.part.name
    # Replace spaces with underscores and ensure lowercase
    category_name = category_name.replace(' ', '_').lower()
    # Generate a unique filename
    filename = f"{uuid.uuid4().hex}-{filename}"
    # Return the upload path
    return os.path.join('songs_docs', category_name,filename)
class Copies(models.Model):
    id=models.UUIDField(primary_key=True,default=uuid.uuid4,editable=False)
    name=models.CharField(max_length=255,null=False)
    composer=models.CharField(max_length=255,null=False)
    part=models.ForeignKey(SongCategory,null=True,on_delete=models.CASCADE)
    uploader=models.ForeignKey(Users,on_delete=models.CASCADE,null=True,default='')
    document=models.FileField(upload_to=song_upload_path)
    category=models.ForeignKey(SongType,on_delete=models.CASCADE,null=True,default='')
    def __str__(self):
        return self.name


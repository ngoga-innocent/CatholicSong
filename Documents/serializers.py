from rest_framework import serializers
from .models import Copies,SongType
from Accounts.models import Users
class CopiesSerializer(serializers.ModelSerializer):
    document=serializers.FileField()
    uploader=serializers.PrimaryKeyRelatedField(queryset=Users.objects.all())
    class Meta:
        model=Copies
        fields='__all__'
class SongTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model=SongType
        fields='__all__'
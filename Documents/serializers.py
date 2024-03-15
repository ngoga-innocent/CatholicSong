from rest_framework import serializers
from .models import Copies
from Accounts.models import Users
class CopiesSerializer(serializers.ModelSerializer):
    document=serializers.FileField()
    uploader=serializers.PrimaryKeyRelatedField(queryset=Users.objects.all())
    class Meta:
        model=Copies
        fields='__all__'
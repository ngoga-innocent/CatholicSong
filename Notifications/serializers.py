from rest_framework import serializers
from .models import NotificationModal
class NotificationSeriazer(serializers.ModelSerializer):
    class Meta:
        model=NotificationModal
        fields='__all__'

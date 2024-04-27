from django.db.models.signals import post_save,pre_save
from django.dispatch import receiver
from .models import NotificationModal

@receiver(pre_save,sender=NotificationModal)
def created_notification(instance,sender,**kwargs):
    pass
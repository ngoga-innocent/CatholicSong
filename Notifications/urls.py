from django.urls import path
from .views import NotificationView
urlpatterns = [
    path('',NotificationView.as_view(),name='notification'),
    path('<uuid:pk>',NotificationView.as_view(),name='notification_update')
    
    # path('Gettypes/<uuid:type_id>',SongTypeClass.as_view(),name='song_type')
    # path('<uuid:copy_id>',CopiesClass.as_view(),name='copies')
]
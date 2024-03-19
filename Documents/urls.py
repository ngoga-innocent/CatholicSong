from django.urls import path
from .views import CopiesClass,SongTypeClass
urlpatterns = [
    path('',CopiesClass.as_view(),name='copies'),
    path('Gettypes/',SongTypeClass.as_view(),name='type'),
    # path('Gettypes/<uuid:type_id>',SongTypeClass.as_view(),name='song_type')
    # path('<uuid:copy_id>',CopiesClass.as_view(),name='copies')
]
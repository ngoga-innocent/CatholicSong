from django.urls import path
from .views import MusicianView
urlpatterns = [
    path('',MusicianView.as_view(),name='copies'),
   
]
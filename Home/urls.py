from django.urls import path
from .views import HomeView
urlpatterns = [
    path('privacy',HomeView,name='privacy'),
   
    
]

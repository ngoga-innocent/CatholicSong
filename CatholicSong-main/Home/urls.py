from django.urls import path
from .views import HomeView,Home
urlpatterns = [
    path('',Home.as_view(),name='home'),
    path('privacy',HomeView,name='privacy'),
    
    
]

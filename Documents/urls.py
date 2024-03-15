from django.urls import path
from .views import CopiesClass
urlpatterns = [
    path('',CopiesClass.as_view(),name='copies'),
    # path('<uuid:copy_id>',CopiesClass.as_view(),name='copies')
]
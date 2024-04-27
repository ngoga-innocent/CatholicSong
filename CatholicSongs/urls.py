
from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path('admin/', admin.site.urls),
    path('account/',include('Accounts.urls'),name='account'),
    path('documents/',include('Documents.urls'),name='documents'),
    path('musician/',include('Musicians.urls'),name='musician'),
    path('advertise/',include('Advertise.urls'),name='advertise'),
    path('notification/',include('Notifications.urls'),name='notification')
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
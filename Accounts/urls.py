from django.urls import path
from .views import RegisterView,LoginView,TokenVerification,ResetPassword
urlpatterns = [
    path('Register',RegisterView.as_view(),name='register'),
    path('Login',LoginView.as_view(),name='login'),
    path('TokenVerification',TokenVerification,name='token_verification'),
    path('reset_password',ResetPassword,name='reset_password')
    
]

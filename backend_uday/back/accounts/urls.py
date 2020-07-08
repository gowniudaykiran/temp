from django.urls import path,include,re_path
from .views import CustomRegisterView
from rest_auth.registration.views import VerifyEmailView, RegisterView
urlpatterns = [
    path('',include('allauth.urls')),
    path('',include('rest_auth.urls')),
    path('register/',CustomRegisterView.as_view()),
    
  
]
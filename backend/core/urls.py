from django.urls import path
from .views import RegisterUser

urlPatterns = [
  path('auth/signup', RegisterUser.as_view())
]
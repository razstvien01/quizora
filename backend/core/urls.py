from django.urls import path
from .views import AuthUser

urlpatterns = [
  path('auth/', AuthUser.as_view(), name='auth-register')
]
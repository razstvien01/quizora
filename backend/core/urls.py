from django.urls import path
from .views import RegisterUser

urlpatterns = [
  path('auth/signup/', RegisterUser.as_view(), name='auth-signup')
]
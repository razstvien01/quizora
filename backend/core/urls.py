from django.urls import path
from .views import RegisterAuth0User

urlPatterns = [
  path('users/auth0', RegisterAuth0User.as_view())
]
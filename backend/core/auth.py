import json
import requests
from jose import jwt
from django.conf import settings
from rest_framework.exceptions import AuthenticationFailed

#* Auth0 Config
AUTH0_DOMAIN = settings.AUTH0_DOMAIN
API_IDENTIFIER = settings.AUTH0_API_IDENTIFIER
ALGORITHMS = ["RS256"]

def get_token_auth_header(request):
  """
  * Extracts the JWT token from the Authorization header.
  * Must be in the format: "Authorization: Bearer <token>"
  * Returns just the token part
  """
  auth = request.headers.get("Authorization", None)
  if not auth:
    raise AuthenticationFailed("Authorization header is expected.")
  
  parts = auth.split()
  
  if parts[0].lower() != "bearer":
    raise AuthenticationFailed("Authorization header must start with Bearer")
  elif len(parts) == 1:
    raise AuthenticationFailed("Token not found.")
  elif len(parts) > 2:
    raise AuthenticationFailed("Authorization header must be Bearer token.")
  
  return parts[1]
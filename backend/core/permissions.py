from rest_framework.permissions import BasePermission
from core.auth import get_token_auth_header, decode_jwt

class IsAuth0User(BasePermission):
  def has_permission(self, request, view):
    try:
      token = get_token_auth_header(request)
      payload = decode_jwt(token)
      request.user_paylod = payload
      
      return True
    except Exception as e:
      return False
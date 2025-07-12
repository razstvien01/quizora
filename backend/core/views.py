from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from users.models import User
from .auth import get_token_auth_header, decode_jwt, fetch_user_info
from core.constants import ALLOWED_ROLES

class AuthUser(APIView):
  permission_classes = [AllowAny]
  
  def post(self, request):
    token = get_token_auth_header(request)
    payload = decode_jwt(token)
    user_info = fetch_user_info(token)
    
    email = user_info.get("email")
    name = user_info.get("name", "")
    role = "student"
    
    if not email:
      return Response(
        {"error": "Email not found in token payload"},
        status=400
      )
    
    if role not in ALLOWED_ROLES:
      role = 'student'
    
    user, created = User.objects.get_or_create(
      auth_id = payload['sub'],
      defaults={
        'email': email,
        'name': name,
        'role': role
      }
    )
    
    return Response({
      "id": user.id,
      "email": user.email,
      "name": user.name,
      "role": user.role,
      "new": created
    })
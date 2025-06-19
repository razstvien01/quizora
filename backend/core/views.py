from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from .models import Auth0User
from .auth import get_token_auth_header, decode_jwt

class RegisterAuth0User(APIView):
  permission_classes = [AllowAny]
  
  def post(self, request):
    token = get_token_auth_header(request)
    payload = decode_jwt(token)
    
    user, created = Auth0User.objects.get_or_create(
      auth0_id = payload['sub'],
      defaults={
        'email': payload['email'],
        'name': payload.get('name', ''),
        'role': 'student'  # default role
      }
    )
    
    return Response({
      "id": user.id,
      "email": user.email,
      "name": user.name,
      "role": user.role,
      "new": created
    })
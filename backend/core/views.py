from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from users.dto import UserDto, UserIdentityDto
from core.services import CoreService

class AuthUser(APIView):
    permission_classes = [AllowAny]
    
    def post(self, request):
        data = request.data
        
        email = data.get("email")
        provider = data.get("provider")
        auth_id = data.get("auth_id")
        
        if not email or not provider or not auth_id:
            return Response({"error": "Missing required fields"}, status=400)
        
        user_dto = UserDto(
            email=email,
            first_name=data.get("first_name", ""),
            last_name=data.get("picture"),
            is_active=True,
            is_superuser=False,
            role=data.get("role", "student")
        )
        
        identity_dto = UserIdentityDto(
            provider=provider,
            auth_id=auth_id,
            user=None
        )
        
        created_user = CoreService.update_or_create_user(user_dto, identity_dto)
        
        return Response({
            "message": "User created or updated",
            "user_id": created_user.id
        })
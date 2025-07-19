from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from core.services.core_service import CoreService
from users.dto.user_dto import UserDto
class AuthUser(APIView):
    permission_classes = [AllowAny]
    
    def post(self, request):
        data = request.data
        user_dto = UserDto(
            email=data['email'],
            first_name=data['first_name'],
            last_name=data['last_name'],
            picture=data.get('picture'),
            is_active=True,
            is_super_user=False,
            role=data.get('role', 'user'),
            auth_id=data['auth_id'],
        )
        
        if not user_dto.email or not user_dto.auth_id:
            return Response({
                "error": "Missing required fields"},
                status=400
            )
            
        created_user = CoreService.update_or_create_user(user_dto)
        
        return Response({
            "message": "User created",
            "user_id": created_user.id 
        })
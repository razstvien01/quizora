from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from rest_framework import status
from users.dto import UserDto, UserIdentityDto
from core.services import CoreService
from users.serializers import UserSerializer
import logging

logger = logging.getLogger(__name__)

class AuthUser(APIView):
    permission_classes = [AllowAny]
    
    def post(self, request):
        try:
            data = request.data
            logger.info("AuthUser POST data received: %s", data)
            
            email = data.get("email")
            provider = data.get("provider")
            auth_id = data.get("auth_id")
            
            missing = [key for key in ['email', 'provider', 'auth_id'] if not data.get(key)]
            if missing:
                return Response(
                    {"error": f"Missing required fields: {', '.join(missing)}"},
                    status=status.HTTP_400_BAD_REQUEST
                )
            
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
            
            serialized_user = UserSerializer(created_user)
            
            logger.info("User successfully created or updated: ID=%s", created_user.id)
            
            return Response(
                {
                    "message": "User created or updated",
                    "user": serialized_user.data
                },
                status=status.HTTP_200_OK
            )
        except Exception as e:
            logger.exception("Exception in AuthUser view")
            return Response(
                {
                    "error": "An unexpected error occured",
                    "details": str(e)
                },
                status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )
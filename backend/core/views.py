from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from core.services.core_service import CoreService
class AuthUser(APIView):
    permission_classes = [AllowAny]
    
    def post(self, request):
        email = ...
        username = ...
        role = ...
        auth_id = ...
        
        user, created = CoreService.get_or_create_user(email, username, role, auth_id)
        
        return Response({
            "id": user.id,
            "email": user.email,
            "new": created
        })
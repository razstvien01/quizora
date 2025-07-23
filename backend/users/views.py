from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework import status
from users.repositories import UserRepository
from users.serializers import UserSerializer
import logging

logger = logging.getLogger(__name__)

class UserView(APIView):
    permission_classes = [IsAuthenticated]
    
    def get(self, request, id):
        try:
            user = UserRepository.get_by_id(id)
            
            if not user:
                logger.warning(f"User with ID {id} not found.")
                return Response(
                    {"error": "User not found"},
                    status=status.HTTP_404_NOT_FOUND
                )
                
            serialized_user = UserSerializer(user)
            
            logger.info(f"Retrieved user {user.email} with ID {user.id}")
            
            return Response(
                {
                    "message": "Retrieved user.",
                    "user": serialized_user.data
                },
                status=status.HTTP_200_OK
            )
            
        except Exception as e:
            logger.error(f"Error retrieving user by ID {id}: {str(e)}", exc_info=True)
            
            return Response(
                {
                    "error": "Internal server error",
                    "details": str(e)
                },
                status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )
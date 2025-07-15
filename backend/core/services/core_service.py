from core.repositories.core_repository import CoreRepository
from users.repositories.user_repository import UserRepository

class CoreService:
    @staticmethod
    def get_or_create_user(email, name, role, auth_id):
        user = UserRepository.get_by_email(email=email)
        
        if user:
            if user.auth_id != auth_id:
                user = CoreRepository.update_auth_id(user, auth_id)
                
            return user, False
        else:
            new_user = CoreRepository.create_user(email, name, role, auth_id)
            
            return new_user, True
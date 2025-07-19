from users.models.user import User
from django.db.models import Q

class CoreRepository:
    @staticmethod
    def create_user(user: User):
        return user.save() or user
        
    @staticmethod
    def update_auth_id(user: User, auth_id: str):
        user.auth_id = auth_id
        user.save()
        return user
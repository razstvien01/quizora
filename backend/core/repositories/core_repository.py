from users.models import User
from django.db.models import Q

class CoreRepository:
    @staticmethod
    def create_user(email, username, role, auth_id):
        return User.objects.create(
            email=email,
            username=username,
            role=role,
            auth_id=auth_id
        )
        
    @staticmethod
    def update_auth_id(user: User, auth_id: str):
        user.auth_id = auth_id
        user.save()
        return user
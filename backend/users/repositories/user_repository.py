from users.models.user import User

class UserRepository:
    @staticmethod
    def get_by_email(email: str):
        return User.objects.filter(email=email).first()
    
    @staticmethod
    def get_by_auth_id(auth_id: str):
        return User.objects.filter(auth_id=auth_id).first()
    
    @staticmethod
    def get_by_id(id: int):
        return User.objects.filter(id=id).first()
    
    @staticmethod
    def get_all() -> list[User]:
        return list(User.objects.all())
    
    @staticmethod
    def create_user(user: User):
        return user.save() or user
    
    @staticmethod
    def save(user: User) -> User:
        user.save()
        return user
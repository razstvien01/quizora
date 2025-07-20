from users.dto.user_dto import UserDto
from users.models.user import User
from users.models.identity import UserIdentity

class UserMapper:
    @staticmethod
    def create_user_from_dto(dto: UserDto) -> User:
        return User(
            email=dto.email,
            first_name=dto.first_name,
            last_name=dto.last_name,
            picture=dto.picture,
            is_active=dto.is_active,
            is_super_user=dto.is_super_user,
            role=dto.role,
            auth_id=dto.auth_id,
        )
        
    @staticmethod
    def user_model_to_dto(user: User) -> UserDto:
        return UserDto(
            email=user.email,
            first_name=user.first_name,
            last_name=user.last_name,
            picture=user.picture,
            is_active=user.is_active,
            is_super_user=user.is_super_user,
            role=user.role,
            auth_id=user.auth_id
        )
        
    @staticmethod
    def update_model_from_dto(user: User, dto: UserDto) -> User:
        user.first_name = dto.first_name
        user.last_name = dto.last_name
        user.picture = dto.picture
        user.is_active = dto.is_active
        user.is_superuser = dto.is_superuser
        user.role = dto.role
        
        return user;
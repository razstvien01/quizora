from users.repositories import UserIdentityRepository, UserRepository
from users.dto import UserDto, UserIdentityDto
from users.models import User, UserIdentity
from users.mappers import UserMapper, UserIdentityMMapper

class CoreService:
    @staticmethod
    def update_or_create_user(user_dto: UserDto, identity_dto: UserIdentityDto) -> User:
        identity = UserIdentityRepository.get_by_provider_and_auth_id(
            provider=identity_dto.provider,
            auth_id=identity_dto.auth_id
        )
        
        if identity:
            user = identity.user
            user = UserMapper.update_model_from_dto(user, user_dto)
        else:
            user = UserMapper.create_user_from_dto(user_dto)
            
        UserRepository.save(user)
        
        if not identity:
            identity_dto.user = user
            identity = UserIdentityMMapper.from_dto(identity_dto)
            UserIdentityRepository.save(identity)
            
        return user
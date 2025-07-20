from users.models import UserIdentity
from users.dto import UserIdentityDto

class UserIdentityMMapper:
    @staticmethod
    def from_dto(dto: UserIdentityDto) -> UserIdentity:
        return UserIdentity(
            provider = dto.provider,
            auth_id = dto.auth_id,
            user = dto.user
        )
        
    @staticmethod
    def to_dto(identity: UserIdentity) -> UserIdentityDto:
        return UserIdentityDto(
            provider = identity.provider,
            auth_id = identity.auth_id,
            user= identity.user
        )
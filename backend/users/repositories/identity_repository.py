from users.models import UserIdentity

class UserIdentityRepository:
    @staticmethod
    def get_by_provider_and_auth_id(provider: str, auth_id: str):
        try:
            return UserIdentity.objects.get(provider=provider, auth_id=auth_id)
        except UserIdentity.DoesNotExist:
            return None
        
    @staticmethod
    def save(identity: UserIdentity) -> UserIdentity:
        identity.save()
        return identity
from dataclasses import dataclass
from typing import Optional
from users.models import User

@dataclass
class UserIdentityDto:
    provider: str
    auth_id: str
    user: Optional[User] = None
from dataclasses import dataclass, field
from typing import Optional

@dataclass(frozen=True)
class UserDto:
    email: str
    first_name: str
    last_name: str
    picture: Optional[str] = None
    is_active: bool = True
    is_superuser: bool = False
    role: str = "user"
    auth_id: str = field(default_factory=str)
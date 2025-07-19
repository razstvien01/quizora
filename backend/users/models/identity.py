from django.db import models
import uuid
from users.models.user import User

class UserIdentity(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    provider = models.CharField(max_length=64)
    auth_id = models.CharField(max_length=255)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='identities')
    created_at = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        unique_together = ('provider', 'auth_id') 
        db_table = 'user_identities'
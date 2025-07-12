import uuid
from django.db import models

from backend.users.models import User

class UserSettings(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='settings')
    receive_notifications = models.BooleanField(default=True)
    theme_preference = models.CharField(max_length=50, choices=[("light", "Light"), ("dark", "Dark")], default="light")
    language = models.CharField(max_length=20, default='en')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return f"UserSettings {id}"
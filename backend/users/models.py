from django.db import models
from django.contrib.auth.models import AbstractUser
import uuid

class User(AbstractUser):
  id = models.UUIDField(primary_key=True, editable=False, default=uuid.uuid4)
  auth_id = models.CharField(max_length=128, unique=True)
  email = models.EmailField()
  name = models.CharField(max_length=255)
  role = models.CharField(max_length=64, default='student')
  created_at = models.DateTimeField(auto_now_add=True)
  updated_at = models.DateTimeField(auto_now=True)
  
  def __str__(self):
    return f"User {self.email} ({self.role})"
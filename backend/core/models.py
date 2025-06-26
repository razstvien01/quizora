from django.db import models

class User(models.Model):
  auth_id = models.CharField(max_length=128, unique=True)
  email = models.EmailField()
  name = models.CharField(max_length=255)
  role = models.CharField(max_length=64, default='student')
  
  def __str__(self):
    return self.email
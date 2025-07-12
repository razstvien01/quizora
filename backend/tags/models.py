import uuid
from django.db import models

from backend.mock_quizzes.models import MockQuiz


class Tag(models.Model):
  id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
  name = models.CharField(max_length=50, unique=True)
  created_at = models.DateTimeField(auto_now_add=True)
  updated_at = models.DateTimeField(auto_now=True)
  
  def __str__(self):
    return f"Tag {self.id} - {self.name}"
  
class MockQuizTag(models.Model):
  mock_quiz = models.ForeignKey(MockQuiz, on_delete=models.CASCADE)
  tag = models.ForeignKey(Tag, on_delete=models.CASCADE)
  
  def __str__(self):
    return f"MockQuizTag {self.mock_quiz} - {self.tag}"
  
  class Meta:
    unique_together = ('mock_quiz', 'tag')
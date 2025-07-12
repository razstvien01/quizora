import uuid
from django.db import models

from mock_quizzes.models import MockQuiz
from users.models import User

class Attempt(models.Model): 
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user = models.ForeignKey(User, related_name='attempts', on_delete=models.CASCADE)
    mock_quiz = models.ForeignKey(MockQuiz, related_name='attempts', on_delete=models.CASCADE)
    score = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)
    started_at = models.DateTimeField(auto_now_add=True)
    completed_at = models.DateTimeField(null=True, blank=True)
    answers = models.JSONField()
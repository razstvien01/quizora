from django.db import models

from mock_quizzes.models import MockQuiz
from tags.models.tag import Tag

class MockQuizTag(models.Model):
    mock_quiz = models.ForeignKey(MockQuiz, on_delete=models.CASCADE)
    tag = models.ForeignKey(Tag, on_delete=models.CASCADE)
    
    def __str__(self):
        return f"MockQuizTag {self.mock_quiz} - {self.tag}"
    
    class Meta:
        unique_together = ('mock_quiz', 'tag')
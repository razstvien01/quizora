import uuid
from django.db import models
from backend.mock_quizzes.models import MockQuiz
from django.core.exceptions import ValidationError

class Questions(models.Model):
    QUESTION_TYPES = (
        ('MCQ', 'Multiple Choice'),
        ('TF', 'True/False'),
        ('FIB', 'Fill in the Blank'),
        ('SA', 'Short Answer'),
        ('ESSAY', 'Essay / Long Answer'),
        ('CODE', 'Code Snippet'),
        ('IDF', 'Identification'),
        ('MATCH', 'Matching'),
        ('ORDER', 'Ordering'),
        ('MA', 'Multiple Answers'),
        ('OTH', 'Other'),
    )

    
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    mock_exam = models.ForeignKey(MockQuiz, related_name='questions', on_delete=models.CASCADE)
    text = models.TextField()
    type = models.CharField(max_length=10, choices=QUESTION_TYPES)
    #? Required for MCQ, MATCH, ORDER
    choices = models.JSONField(blank=True, null=True)
    #? Handle arrays for MATCH, ORDER, and other types
    correct_answer = models.JSONField(blank=True, null=True)
    explanation = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def clean(self):
        #? Validation Logic
        if self.type in ['MCQ', 'MATCH', 'ORDER', 'MA'] and not self.choices:
            raise ValidationError(f"Choices are required for {self.get_type_display()} type.")
        if self.type in ['MCQ', 'TF', 'FIB', 'IDF'] and not self.correct_answers:
            raise ValidationError(f"Correct answers are required for {self.get_type_display()} type.")
        if self.type == 'TF':
            valid_tf = ['True', 'False', True, False]
            if self.correct_answers not in valid_tf and str(self.correct_answers).lower() not in ['true', 'false']:
                raise ValidationError("True/False questions must have corrrect answer of 'True' or 'False'.")
            
    def __str__(self):
        return f"Question {self.id} - {self.text[:50]}"
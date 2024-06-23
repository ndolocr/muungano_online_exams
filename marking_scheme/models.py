from django.db import models
from question.models import Question
# Create your models here.

class MarkingScheme(models.Model):
    correct_answer = models.TextField()

    question = models.ForeignKey(Question, on_delete=models.CASCADE, null=False, blank=False)

    updated_on = models.DateTimeField(auto_now=True)
    created_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.question
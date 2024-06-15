from django.db import models

from question.models import Question

# Create your models here.

class MultipleChoice(models.Model):
    answer = models.TextField()
    Choice = models.CharField(max_length=5, null = False, blank = False)
    
    question = models.ForeignKey(Question, on_delete=models.CASCADE, null=False, blank=False)

    updated_on = models.DateTimeField(auto_now=True)
    created_on = models.DateTimeField(auto_now_add=True)
from django.db import models

from tags.models import Tag
from image.models import Image
from passage.models import Passage
from examination_paper.models import ExaminationPaper

# Create your models here.

class Question(models.Model):
    question = models.TextField()
    marks = models.IntegerField()
    question_number = models.IntegerField()
    parent_question = models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True)

    tags = models.ManyToManyField(Tag)

    image = models.ForeignKey(Image, on_delete=models.CASCADE, null=True, blank=True)
    passage = models.ForeignKey(Passage, on_delete=models.CASCADE, null=True, blank=True)
    examination_paper = models.ForeignKey(ExaminationPaper, on_delete=models.CASCADE, null=False, blank=False)

    updated_on = models.DateTimeField(auto_now=True)
    created_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.question_number
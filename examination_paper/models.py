from django.db import models

from examination.models import Examination
from instructions.models import Instruction

# Create your models here.
class ExaminationPaper(models.Model):
    year = models.IntegerField()
    exam_duration  = models.DurationField()
    slug = models.SlugField(max_length=255, null = True, blank = True)
    name = models.CharField(max_length=255, null = False, blank = False)
    section = models.SlugField(max_length=255, null = True, blank = True)
    subject = models.SlugField(max_length=255, null = True, blank = True)
    
    examination = models.ForeignKey(Examination, on_delete=models.CASCADE)
    instructions = models.ForeignKey(Instruction, on_delete=models.CASCADE)
    
    updated_on = models.DateTimeField(auto_now=True)
    created_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

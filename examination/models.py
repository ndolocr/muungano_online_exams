from django.db import models

from examination_body.models import ExaminationBody

# Create your models here.
class Examination(models.Model):
    slug = models.SlugField(max_length=255, null = True, blank = True)
    name = models.CharField(max_length=255, null = False, blank = False) # Kenya Certificate of Secondary Education
    acronym = models.CharField(max_length=255, null = False, blank = False) # KCSE
    
    examination_body = models.ForeignKey(ExaminationBody, on_delete=models.CASCADE) #KNEC

    updated_on = models.DateTimeField(auto_now=True)
    created_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.acronym
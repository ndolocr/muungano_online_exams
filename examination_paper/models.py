from django.db import models

from examination.models import Examination

# Create your models here.
class ExaminationPaper(models.Model):
    class Meta:
        db_table = "examination_paper"
    year = models.IntegerField()    
    slug = models.SlugField(max_length=255, null = True, blank = True)
    name = models.CharField(max_length=255, null = False, blank = False) # Paper 1
    # section = models.SlugField(max_length=255, null = True, blank = True)
    subject = models.SlugField(max_length=255, null = True, blank = True)
    exam_duration  = models.CharField(max_length=255, null = True, blank = True)
    
    examination = models.ForeignKey(Examination, on_delete=models.CASCADE, null=False)    
    
    updated_on = models.DateTimeField(auto_now=True)
    created_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
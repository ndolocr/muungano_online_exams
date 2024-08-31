from django.db import models

from user_management.models import User
# Create your models here.

class ExaminationBody(models.Model):
    class Meta:
        db_table = "examination_body"
        
    slug = models.SlugField(max_length=255, null = True, blank = True)
    name = models.CharField(max_length=255, null = False, blank = False)
    acronym = models.CharField(max_length=255, null = False, blank = False)
    created_by = models.ForeignKey(User,on_delete=models.CASCADE,null=True)
    
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.acronym


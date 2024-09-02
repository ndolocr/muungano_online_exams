from django.db import models

from ckeditor.fields import RichTextField
# Create your models here.

class Instruction(models.Model):
    class Meta:
        db_table = "instruction"
    instructions = RichTextField()
    
    updated_on = models.DateTimeField(auto_now=True)
    created_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.instruction_number

from django.db import models

# Create your models here.

class Instruction(models.Model):
    instructions = models.TextField()
    instruction_number = models.IntegerField()
    
    updated_on = models.DateTimeField(auto_now=True)
    created_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.instruction_number

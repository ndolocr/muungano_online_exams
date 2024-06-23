from django.db import models

# Create your models here.
class Table(models.Model):
    table_name = models.CharField(max_length=255, null = False, blank = False)
    no_of_rows = models.CharField(max_length=255, null = False, blank = False)
    no_of_columns = models.CharField(max_length=255, null = False, blank = False)
    
    updated_on = models.DateTimeField(auto_now=True)
    created_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.question_number
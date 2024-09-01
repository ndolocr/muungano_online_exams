from django.db import models
from table.models import Table
# Create your models here.
class CellInformation(models.Model):
    class Meta:
        db_table = "cell_information"
    cell_x = models.IntegerField(null = False, blank = False)
    cell_y = models.IntegerField(null = False, blank = False)
    value = models.CharField(max_length=255, null = True, blank = True)
    table = models.ForeignKey(Table, on_delete=models.CASCADE, null = False, blank = False)
    
    updated_on = models.DateTimeField(auto_now=True)
    created_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.value
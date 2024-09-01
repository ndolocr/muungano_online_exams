from django.db import models

# Create your models here.
class Tag(models.Model):
    class Meta:
        db_table = "tags"
    name = models.CharField(max_length=255, unique=True)

    updated_on = models.DateTimeField(auto_now=True)
    created_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
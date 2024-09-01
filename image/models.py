from django.db import models

# Create your models here.
class Image(models.Model):
    class Meta:
        db_table = "image"
    description = models.TextField()
    url = models.URLField(max_length=225)
    
    updated_on = models.DateTimeField(auto_now=True)
    created_on = models.DateTimeField(auto_now_add=True)
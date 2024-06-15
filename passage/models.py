from django.db import models

# Create your models here.
class Passage(models.Model):
    passage = models.TextField()
    
    updated_on = models.DateTimeField(auto_now=True)
    created_on = models.DateTimeField(auto_now_add=True)
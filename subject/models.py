from django.db import models

# Create your models here.
class Subject(models.Model):
    class Meta:
        db_table = "subject"
    subject = models.CharField(max_length=255, null=False)

    updated_on = models.DateTimeField(auto_now=True)
    created_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.subject
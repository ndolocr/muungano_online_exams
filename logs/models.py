from django.db import models

from user_management.models import User
from examination.models import Examination
from examination_body.models import ExaminationBody
# Create your models here.

class ExaminationLogs(models.Model):
    class Meta:
        db_table = "examination_logs"

    values = models.TextField(null=False)
    action = models.CharField(max_length=255, null=False)    
    examination = models.ForeignKey(Examination, on_delete=models.CASCADE, related_name="logs_on_examination")
    action_by = models.ForeignKey(User,on_delete=models.CASCADE,null=True, related_name="logs_on_examination_action_by")
    
    updated_on = models.DateTimeField(auto_now=True)    
    created_on = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"{self.action_by.email} - {self.action } - {self.examination_body.acronym}"

class ExaminationBodyLogs(models.Model):
    class Meta:
        db_table = "examination_body_logs"

    values = models.TextField(null=False)
    action = models.CharField(max_length=255, null=False)    
    examination_body = models.ForeignKey(ExaminationBody, on_delete=models.CASCADE, related_name="logs_on_examination_body")
    action_by = models.ForeignKey(User,on_delete=models.CASCADE,null=True, related_name="logs_on_examination_body_action_by")
    
    updated_on = models.DateTimeField(auto_now=True)    
    created_on = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"{self.action_by.email} - {self.action } - {self.examination_body.acronym}"
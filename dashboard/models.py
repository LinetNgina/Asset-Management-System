from django.contrib.auth.models import User
from django.db import models

class MaintenanceRecord(models.Model):
    category = models.CharField(max_length=100)
    asset_id = models.CharField(max_length=50)
    comments = models.TextField()

    def __str__(self):
        return f"{self.category} - {self.asset_id}"

class MaintenanceRequest(models.Model):
    subject = models.CharField(max_length=100)
    description = models.TextField()
    submitted_by = models.ForeignKey(User, on_delete=models.CASCADE)
    submitted_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.subject

class YourModel(models.Model):
    field1 = models.CharField(max_length=100)
    field2 = models.TextField()

    def __str__(self):
        return self.field1
from django.db import models

class Task(models.Model):
    task_name = models.CharField(max_length=50)
    description = models.TextField(max_length=500)
    is_completed = models.BooleanField(default=False)
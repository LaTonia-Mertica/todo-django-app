from django.db import models

# Create your models here.
class Todo(models.Model):
    task_id = models.AutoField(primary_key=True)
    task = models.CharField(max_length=255)
    completed = models.BooleanField(default=False)
    in_progress = models.BooleanField(default=False)
    user = models.CharField(max_length=255, default='noone')


class Note(models.Model):
    note_id = models.AutoField(primary_key=True)
    note_text = models.CharField(max_length=444) 



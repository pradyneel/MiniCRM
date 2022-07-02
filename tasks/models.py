from django.db import models
from main.models import User

# Create your models here.
class Tasks(models.Model):
    task_id = models.CharField(max_length = 50)
    name  = models.CharField(max_length = 50)
    company = models.CharField(max_length = 50)
    date = models.DateField()
    task = models.CharField(max_length = 255)
    status = models.BooleanField()
    user = models.ForeignKey(User, on_delete = models.CASCADE)
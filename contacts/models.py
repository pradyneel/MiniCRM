from django.db import models
from main.models import User

# Contacts model
class Contacts(models.Model):
    contact_id = models.AutoField(primary_key=True)
    Name = models.CharField(max_length = 50)
    Company = models.CharField(max_length = 50)
    Role = models.CharField(max_length = 50)
    PhoneNumber = models.CharField(max_length = 50)
    Email = models.EmailField(max_length=50)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
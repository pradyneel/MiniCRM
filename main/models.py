from django.db import models

# User details
class User(models.Model):
   userEmail = models.EmailField(max_length=50)
   userName = models.CharField(max_length = 50)
   userCompany = models.CharField(max_length = 50)
   password = models.CharField(max_length = 140)




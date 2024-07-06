from django.db import models

# Create your models here.
class SignUp(models.Model):
    username = models.CharField(max_length=30)
    password = models.CharField(max_length=50)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.EmailField(max_length=50)
    
    
from django.db import models
from django.contrib.auth.models import User

# Create your models here.




class Employee(models.Model):
    employee = models.OneToOneField(User, on_delete=models.CASCADE)
    age = models.IntegerField()
    
    def __str__(self) -> str:
        return self.employee.username
   

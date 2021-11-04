from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Employee(models.Model):
    position_choice = [
    ('accounts', 'Accounts'),
    ('director', 'Director'),
    ('project_menager', 'Project Menager'),
]
    
    employee = models.OneToOneField(User, on_delete=models.CASCADE)
    position = models.CharField(max_length=30, null=True, blank=True, choices=position_choice)
    
    def __str__(self) -> str:
        return self.employee.username
   

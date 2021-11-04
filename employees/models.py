from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Employee(models.Model):

    position_choices = [
    ('accounts', 'Accounts'),
    ('director', 'Director'),
    ('project_menager', 'Project menager')
    ]
    
    employee = models.OneToOneField(User, on_delete=models.CASCADE)
    position = models.CharField(max_length=20 ,choices=position_choices, null=True, blank=True)
    
    
    def __str__(self) -> str:
        return self.employee.username
   

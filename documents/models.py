from django.db import models
from django.db.models.deletion import CASCADE
from django.db.models.fields import CharField
from django.contrib.auth.models import User
from employees.models import Employee

# Create your models here.
class Document(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    description = models.TextField(max_length=300, blank=True, null=True)
    created = models.DateTimeField(auto_now_add=True)
    approved = models.BooleanField(default=False, null=True, blank=True)
    document_file = models.FileField(null=True, blank=True)
    
    def __str__(self) -> str:
        return str(self.document_file)
    







    



    
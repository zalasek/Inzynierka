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
    document_file = models.FileField(upload_to='media/', null=True, blank=True)
    
    def __str__(self) -> str:
        return str(self.document_file)

class Project(models.Model):
    owner = models.ForeignKey(User, on_delete=CASCADE)
    title = models.CharField(max_length=500)
    document = models.ForeignKey(Document, on_delete=models.CASCADE)
    description = models.TextField(max_length=1000, null=True, blank=True)

    def __str__(self) -> str:
        return str(self.title)

class Assignment(models.Model):
    project = models.ForeignKey(Project, on_delete=CASCADE)
    user = models.ForeignKey(User, on_delete=CASCADE)
    created = models.DateTimeField(auto_now_add=True)




    



    
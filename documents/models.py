from django.db import models
from django.db.models.deletion import CASCADE
from django.db.models.fields import CharField
from django.contrib.auth.models import User
from employees.models import Employee

# Create your models here.
class Document(models.Model):
    type_choice = [ ('product', 'Product'),
                    ('service', 'Service'),]  # podział faktur na produkt / usługę 
    status_choice = [ ('Waiting for assignment to PM', 'Waiting for assignment to PM'),
                      ('Waiting for checks', 'Waiting for checks'),
                      ('Waiting for director to approve', 'Waiting for director to approve'),
                      ('Waiting for payment', 'Waiting for payment'),
                      ('Paid', 'Paid')
    ]
    
    title = models.CharField(max_length=250, blank=False, null=False, default='')
    owner = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True) # osoba która dodała dokument
    description = models.TextField(max_length=1000, blank=True, null=True) # opis dokumentu
    created = models.DateTimeField(auto_now_add=True) # czas i data stworzenia
    document_file = models.FileField(null=True, blank=True) # plik dokumentu 
    type = models.CharField(max_length=30, null=False, blank=True, choices=type_choice, default='') # rodzaj faktury
    status = models.CharField(max_length=50, null=True, blank=True, choices=status_choice) # obecny status dokumentu

    def __str__(self) -> str:
        return str(self.title)

class Assignment(models.Model):
    document = models.ForeignKey(Document, on_delete=CASCADE, null=True, blank=True) 
    employee = models.ForeignKey(Employee, on_delete=CASCADE, null=True, blank=True, limit_choices_to={'position':'project_menager'})

class Comment(models.Model):
    document = models.ForeignKey(Document, on_delete=CASCADE, null=True, blank=True) 
    employee = models.ForeignKey(Employee, on_delete=CASCADE, null=True, blank=True) 
    comment = models.TextField(blank=False, null=False)
    created = models.DateTimeField(auto_now_add=True)






    



    
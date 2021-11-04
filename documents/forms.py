from django import forms

from .models import Document, Assignment

class DocumentForm(forms.ModelForm):
    class Meta:
        model=Document
        fields = [
            'type',
            'document_file',
            'description',
        ]

class AssignmentForm(forms.ModelForm):
    class Meta:
        model = Assignment
        fields = ['document', 'employee']
        

        
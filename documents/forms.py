from django import forms

from .models import Document

class DocumentForm(forms.ModelForm):
    class Meta:
        model=Document
        fields = [
            'type',
            'document_file',
            'description',
        ]
        

        
from django import forms

from .models import Document

class DocumentForm(forms.ModelForm):
    class Meta:
        model=Document
        fields = [
            'approved',
            'document_file',
        ]
        

        
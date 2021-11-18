from django import forms

from .models import Comment, Document, Assignment

class DocumentForm(forms.ModelForm):
    class Meta:
        model=Document
        fields = ['title',
                  'owner',
                  'description',
                  'approved_director',
                  'approved_pm',
                  'type',
                  'status']
        
class FileForm(forms.ModelForm):
    class Meta:
        model=Document
        fields = ['document_file']

class AssignmentForm(forms.ModelForm):
    class Meta:
        model = Assignment
        fields = ['document', 'employee']
        
class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['comment']
        

        
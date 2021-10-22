from django.shortcuts import render
from .models import Document
# Create your views here.



def DocumentListView(request, *args, **kwargs):
    documents = Document.objects.all()
    context = {'documents' : documents}
    return render(request, 'documents/document_list.html', context)



def DocumentDetailView(request, pk):
    document = Document.objects.get(id=pk)
    context = {'document':document}
    return render(request, 'documents/document_detail.html', context)
    

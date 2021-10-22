from django.shortcuts import redirect, render
from .models import Document
from .forms import DocumentForm
# Create your views here.

def DocumentListView(request, *args, **kwargs):
    documents = Document.objects.all()
    context = {'documents' : documents}
    return render(request, 'documents/document_list.html', context)



def DocumentDetailView(request, pk):
    document = Document.objects.get(id=pk) 
    context = {'document':document}
    return render(request, 'documents/document_detail.html', context)




def DocumentCreateView(request):
    if request.method == 'POST': #gdy zatwierdzimy formularz
        form = DocumentForm(request.POST , request.FILES)
        if form.is_valid():
            form.save()
            return redirect('document-list')   
    else:   
        form = DocumentForm()  #gdy wczytamy stronę z formularzem
    context = {'form':form} 
    return render(request, 'documents/document_create.html', context)

def DocumentDeleteView(request, pk):
    document = Document.objects.get(id=pk)
    if request.method == 'POST':
        document.delete()
        return redirect('document-list')
    context = {'document':document}
    return render(request, 'documents/document_delete.html', context)


def DocumentUpdateView(request, pk):
    document = Document.objects.get(id=pk)
    if request.method == 'POST': #gdy zatwierdzimy formularz
        form = DocumentForm(request.POST , request.FILES)
        if form.is_valid():
            form.update()
            return redirect('document-list')   
    else:   
        form = DocumentForm()  #gdy wczytamy stronę z formularzem
    context = {'form':form} 
    return render(request, 'documents/document_update.html', context)



    
    
    

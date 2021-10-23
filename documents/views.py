from django.shortcuts import redirect, render, get_object_or_404
from .models import Document
from .forms import DocumentForm
from django.core.files.storage import FileSystemStorage






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
    form = DocumentForm(request.POST , request.FILES)
    context = {'form':form}
    if request.method == 'POST':
        document_file = request.FILES['document_file']
        fs = FileSystemStorage()
        document_file = fs.save(document_file.name, document_file)
        Document.objects.filter(id = pk).update(document_file = document_file)
        return redirect('document-list')
    else:
        return render(request, 'documents/document_update.html', context)



    
    
    

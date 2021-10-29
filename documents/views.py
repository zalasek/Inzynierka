from django.shortcuts import redirect, render
from .models import Document
from .forms import DocumentForm
from django.core.files.storage import FileSystemStorage
from django.contrib.auth import authenticate, login, logout 
from django.conf import settings



def DocumentListView(request):
    owner_id = request.user.id
    documents = Document.objects.filter(owner=owner_id)
    context = {'documents' : documents}
    return render(request, 'documents/document_list.html', context)




def DocumentDetailView(request, pk):
    if not request.user.is_authenticated:
        return redirect('login')    
    document = Document.objects.get(id=pk) 
    context = {'document':document}
    return render(request, 'documents/document_detail.html', context)





def DocumentCreateView(request):
    if not request.user.is_authenticated:
        return redirect('login')
    if request.method == 'POST': #gdy zatwierdzimy formularz
        form = DocumentForm(request.POST , request.FILES)
        
        if form.is_valid():
            document = form.save(commit=False)
            document.owner = request.user
            document.save()
            return redirect('document-list')      
    else:   
        form = DocumentForm()  #gdy wczytamy stronę z formularzem
    context = {'form':form} 
    return render(request, 'documents/document_create.html', context)



def DocumentDeleteView(request, pk):
    if not request.user.is_authenticated:
        return redirect('login')   
    document = Document.objects.get(id=pk)
    if request.method == 'POST':
        document.delete()
        return redirect('document-list')
    context = {'document':document}
    return render(request, 'documents/document_delete.html', context)


def DocumentUpdateView(request, pk):
    if not request.user.is_authenticated:
        return redirect('login')
    form = DocumentForm(request.POST , request.FILES)
    context = {'form':form}
    if request.method == 'POST':
        owner = request.POST.get('owner')
        approved = request.POST.get('approved')
        document_file = request.FILES['document_file']
        
        fs = FileSystemStorage()
        document_file = fs.save(document_file.name, document_file)
        
        Document.objects.filter(id = pk).update(document_file = document_file)
        Document.objects.filter(id = pk).update(owner = owner)
        Document.objects.filter(id = pk).update(approved = approved.capitalize())
        return redirect('document-list')
    else:
        return render(request, 'documents/document_update.html', context)
    
    
 
        



    
    
    

from django.shortcuts import redirect, render
from .models import Document, Assignment
from .forms import DocumentForm, AssignmentForm
from django.core.files.storage import FileSystemStorage
from django.contrib.auth import authenticate, login, logout 
from django.conf import settings
from employees.models import Employee



def DocumentListView(request):
    owner_id = request.user.id
    documents = Document.objects.filter(owner=owner_id)

    pm = Employee.objects.filter(position = 'project_menager')
    print(pm[1])
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
            return redirect('accounts_home')      
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
        
        owner = request.user
        type = request.POST.get('type')
        document_file = request.FILES['document_file']
        
        fs = FileSystemStorage()
        document_file = fs.save(document_file.name, document_file)
        
        Document.objects.filter(id = pk).update(type = type)
        Document.objects.filter(id = pk).update(document_file = document_file)
        Document.objects.filter(id = pk).update(owner = owner)
        
        return redirect('document-list')
    else:
        return render(request, 'documents/document_update.html', context)



def DocumentAssignView(request, pk):
    if request.method == 'POST':
        form_assignment = AssignmentForm(request.POST)

        if form_assignment.is_valid():
            assignment = form_assignment.save(commit=False)
            assignment.document = Document.objects.get(id = pk)
            assignment.save()
            return redirect('accounts_home')
    else:
        form_assignment = AssignmentForm()
        context = {'form_assignment':form_assignment}
        return render(request, 'documents/document_assign.html', context)
    
    
 
        



    
    
    

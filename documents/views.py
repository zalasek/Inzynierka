from django.shortcuts import redirect, render
from .models import Comment, Document, Assignment
from .forms import DocumentForm, AssignmentForm, FileForm, CommentForm
from django.core.files.storage import FileSystemStorage
from django.contrib.auth import authenticate, login, logout 
from django.conf import settings
from employees.models import Employee



def DocumentListView(request):
    if not request.user.is_authenticated:
        return redirect('login')     
    documents = Document.objects.all()
    context = {'documents' : documents}
    return render(request, 'documents/document_list.html', context)

# def DocumentPersonalListView(request):
#     if not request.user.is_authenticated:
#         return redirect('login')    
#     owner_id = request.user.id
#     documents = Document.objects.filter(owner=owner_id)

#     context = {'documents' : documents}
#     return render(request, 'documents/document_list.html', context)


def DocumentDetailView(request, pk):
    if not request.user.is_authenticated:
        return redirect('login')    
    
    #KUUUUUUUUURRRRRRWWWWWWWWWWAAAAAAAAAAAAA
    document = Document.objects.get(id=pk)
    #print(Document.comment)
    
    if Document.objects.filter(id=pk).exists():
        comment = Document.objects.get(id=pk) 
        context = {'document':document,
                    'comments':comment}
        print('lol')
    else:    
        context = {'document':document}
        
    print(context)
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
    document = Document.objects.get(id = pk)
    initial_data = {
        'title':  document.title,
        'owner':  document.owner, 
        'description': document.description,  
        'approved_director': document.approved_director,  
        'approved_pm':  document.approved_pm, 
        'document_file': document.document_file, 
        'type': document.type, 
        'status': document.status 
    }
    print(initial_data.get('document_file'))
    form = DocumentForm(initial=initial_data)
    file_form = FileForm(request.FILES)
    context = {'form':form, 'file_form':file_form}
    if request.method == 'POST':
        
        title = request.POST['title']
        owner = request.POST['owner']
        description = request.POST['description']
        approved_director = request.POST['approved_director']
        approved_pm = request.POST['approved_pm']
        type = request.POST['type']
        status = request.POST['status']
  
        if  bool(request.FILES.get('document_file', False)) == True:
            document_file = request.FILES['document_file']
            fs = FileSystemStorage()
            document_file = fs.save(document_file.name, document_file)
            Document.objects.filter(id = pk).update(document_file = document_file)
        
        Document.objects.filter(id = pk).update(title = title)
        Document.objects.filter(id = pk).update(owner = owner)
        Document.objects.filter(id = pk).update(description = description)
        Document.objects.filter(id = pk).update(approved_director = approved_director)
        Document.objects.filter(id = pk).update(approved_pm = approved_pm)
        Document.objects.filter(id = pk).update(status = status)
        
        return redirect('document-list')
    else:
        return render(request, 'documents/document_update.html', context)


def DocumentAssignView(request, pk):
    if not request.user.is_authenticated:
        return redirect('login')
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
    
    
def DocumentCommentView(request, pk):
    if not request.user.is_authenticated:
        return redirect('login') 
       
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.document = Document.objects.get(id = pk)
            comment.employee = Employee.objects.get(employee = request.user)
            comment.save()
            return redirect('login') 
    else:
        form = CommentForm()
        context = {'form':form}
        return render(request, 'documents/document_comment.html', context)
    

    
 
        



    
    
    

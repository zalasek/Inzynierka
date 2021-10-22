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
    if request.method == 'POST':
        form = DocumentForm(request.POST , request.FILES)
        if form.is_valid():
            form.save()
            return redirect('document-list')   
    else:   
        form = DocumentForm()  
    context = {'form':form} 
    return render(request, 'documents/document_create.html', context)



    
    
    

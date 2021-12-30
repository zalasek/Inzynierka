from django.shortcuts import redirect, render
from .models import Comment, Document, Assignment
from .forms import DocumentForm, AssignmentForm, FileForm, CommentForm
from django.core.files.storage import FileSystemStorage
from django.contrib.auth import authenticate, login, logout
from django.conf import settings
from employees.models import Employee



################### UNIVERSAL ##################

def DocumentCommentView(request, pk):
    if not request.user.is_authenticated:
        return redirect('login')

    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.document = Document.objects.get(id=pk)
            comment.employee = Employee.objects.get(employee=request.user)
            comment.save()
            return redirect('login')
    else:
        form = CommentForm()
        context = {'form': form}
        return render(request, 'documents/document_comment.html', context)



################ ACCOUNTS ########################

def DocumentDetailAccountsView(request, pk):
    if not request.user.is_authenticated:
        return redirect('login')
    document = Document.objects.get(id=pk)

    if Comment.objects.filter(document=document).exists():
        comments = Comment.objects.filter(document=document)
        context = {'document': document,
                   'comments': comments}
    else:
        context = {'document': document}
    return render(request, 'documents/accounts/document_detail_accounts.html', context)

def DocumentListAccountsView(request):
    if not request.user.is_authenticated:
        return redirect('login')
    documents = Document.objects.all()
    context = {'documents': documents}
    return render(request, 'documents/accounts/document_list_accounts.html', context)


def DocumentCreateAccountsView(request):
    if not request.user.is_authenticated:
        return redirect('login')
    if request.method == 'POST':  # gdy zatwierdzimy formularz
        form = DocumentForm(request.POST)
        file_form = FileForm(request.FILES)
        if form.is_valid() and bool(request.FILES.get('document_file', False)) == True:
            document = form.save(commit=False)
            if document.type == '':
                return redirect('document-create')
            else:
                document.owner = request.user
                document.status = 'Assigned to director'
                document_file = request.FILES['document_file']
                fs = FileSystemStorage()
                document_file = fs.save(document_file.name, document_file)
                document.document_file = document_file
                document.save()
                return redirect('document-list')
    else:
        form = DocumentForm()  # gdy wczytamy stronę z formularzem
        file_form = FileForm()
    context = {'form': form, 'file_form': file_form}
    return render(request, 'documents/accounts/document_create_accounts.html', context)


def DocumentDeleteAccountsView(request, pk):
    if not request.user.is_authenticated:
        return redirect('login')
    document = Document.objects.get(id=pk)
    if request.method == 'POST':
        document.delete()
        return redirect('document-list')
    context = {'document': document}
    return render(request, 'documents/accounts/document_delete_accounts.html', context)


def DocumentUpdateAccountsView(request, pk):
    if not request.user.is_authenticated:
        return redirect('login')
    document = Document.objects.get(id=pk)
    initial_data = {
        'title':  document.title,
        'owner':  document.owner,
        'description': document.description,
        'approved_director': document.approved_director,
        'approved_pm':  document.approved_pm,
        'document_file': document.document_file,
        'type': document.type,
        'status': document.status }

    form = DocumentForm(initial=initial_data)
    file_form = FileForm(request.FILES)
    context = {'form': form, 'file_form': file_form}

    if request.method == 'POST':
        title = request.POST['title']
        description = request.POST['description']
        type = request.POST['type']
        status = request.POST['status']

        if bool(request.FILES.get('document_file', False)) == True:
            document_file = request.FILES['document_file']
            fs = FileSystemStorage()
            document_file = fs.save(document_file.name, document_file)
            Document.objects.filter(id=pk).update(document_file=document_file)

        Document.objects.filter(id=pk).update(title=title)
        Document.objects.filter(id=pk).update(description=description)
        Document.objects.filter(id=pk).update(status=status)
        # dodać
        return redirect('document-list')
    else:
        return render(request, 'documents/accounts/document_update_accounts.html', context)


def DocumentListFinishedAccountsView(request):
    if not request.user.is_authenticated:
        return redirect('login')
    documents = Document.objects.filter(status='Paid')
    context = {'documents':documents}
    return render(request, 'documents/accounts/document_list_finished_accounts.html', context)


def DocumentListWaitingPaymentAccountsView(request):
    if not request.user.is_authenticated:
        return redirect('login')
    if request.method == 'POST':
        id_document = request.POST.get('id')
        request.session['id_document'] = id_document 
        documents = Document.objects.filter(status='Waiting for payment')
        context = {'documents':documents}
        return redirect('document-payment')
    else:
        documents = Document.objects.filter(status='Waiting for payment')
        context = {'documents':documents}
        return render(request, 'documents/accounts/document_list_waiting_payment_accounts.html', context)

def DocumentPaymentView(request):
    if not request.user.is_authenticated:
        return redirect('login')
    if request.method == 'POST':
        id_document  = request.session['id_document'] 
        del request.session['id_document'] 
        Document.objects.filter(id=id_document).update(status='Paid')
        return redirect('document-list-finished')
    context={}
    return render(request, 'documents/accounts/document_payment.html', context)



####################### DIRECTOR ########################
def DocumentDetailDirectorView(request, pk):
    if not request.user.is_authenticated:
        return redirect('login')
    document = Document.objects.get(id=pk)

    if Comment.objects.filter(document=document).exists():
        comments = Comment.objects.filter(document=document)
        context = {'document': document,
                   'comments': comments}
    else:
        context = {'document': document}
    return render(request, 'documents/director/document_detail_director.html', context)

def DocumentAssignView(request):
    if not request.user.is_authenticated:
        return redirect('login')
    if request.method == 'POST':
        id_document = request.session['id_document']
        id_employee = request.session['id_employee']
        del request.session['id_document']
        del request.session['id_employee']
        document = Document.objects.get(id=id_document)
        employee = Employee.objects.get(id=id_employee)
        assignment = Assignment(document=document, employee=employee)
        assignment.save()
        Document.objects.filter(id=id_document).update(status='Waiting')
        return redirect('document-waiting-approval')
        
    context = {}
    return render(request, 'documents/director/document_assign.html', context)

def DocumentApproveView(request):
    if not request.user.is_authenticated:
        return redirect('login')
    if request.method == 'POST':
        id_document = request.session['id_document']
        Document.objects.filter(id=id_document).update(status='Waiting for payment')
        del request.session['id_document']
        return redirect('document-waiting-approval')
    context = {}
    return render(request, 'documents/director/document_approve.html', context)



def DocumentListNotAssignedDirectorView(request):
    if not request.user.is_authenticated:
        return redirect('login')
    documents = Document.objects.filter(status='Assigned to director')
    form_assignment = AssignmentForm(request.POST)
    
    if request.method == 'POST':
        form_assignment = form_assignment.save(commit=False)
        employee = form_assignment.employee
        if employee is not None:
            id_document = request.POST.get('id')
            request.session['id_document'] = id_document
            request.session['id_employee'] = employee.id
            return redirect('document-assign')
        else:
            form_assignment = AssignmentForm()
            context = {'documents':documents, 'form_assignment': form_assignment}
            return render(request, 'documents/director/document_list_not_assigned_director.html', context) 

    context = {'documents':documents, 'form_assignment': form_assignment}
    return render(request, 'documents/director/document_list_not_assigned_director.html', context)


def DocumentListWaitingReturnDirectorView(request):
    if not request.user.is_authenticated:
        return redirect('login')
    documents = Document.objects.filter(status='Waiting')
    context = {'documents':documents}
    return render(request, 'documents/director/document_list_waiting_return_director.html', context)


def DocumentListWaitingApprovalView(request):
    if not request.user.is_authenticated:
        return redirect('login')
    if request.method == 'POST':
        id_document = request.POST.get('id')
        request.session['id_document'] = id_document
        return redirect('document-approve')
    documents = Document.objects.filter(status='Checked')
    context = {'documents':documents}
    return render(request, 'documents/director/document_list_waiting_approval.html', context)



def DocumentConfirmationApprovalView(request, pk):
    if not request.user.is_authenticated:
        return redirect('login')
    document = Document.objects.get(id=pk)
    if request.method == 'POST':
        Document.objects.filter(id=pk).update(status='Waiting for payment')
        return redirect('document-list')
    context = {'document': document}
    return render(request, 'documents/director/document_approval_confirmation.html', context)


############# PM ################
def DocumentDetailPmView(request, pk):
    if not request.user.is_authenticated:
        return redirect('login')
    document = Document.objects.get(id=pk)

    if Comment.objects.filter(document=document).exists():
        comments = Comment.objects.filter(document=document)
        context = {'document': document,
                   'comments': comments}
    else:
        context = {'document': document}
    return render(request, 'documents/pm/document_detail_pm.html', context)

def DocumentWaitingChecksView(request):
    if not request.user.is_authenticated:
        return redirect('login')

    documents = Document.objects.filter(status='Waiting')
    if request.method == 'POST':
        id_document = request.POST.get('id')
        request.session['id_document'] = id_document
        return redirect('document-check')       
    context = {'documents':documents}
    return render(request, 'documents/pm/document_waiting_checks_pm.html', context)


def DocumentCheckedView(request):
    if not request.user.is_authenticated:
        return redirect('login')
    
    documents = Document.objects.filter(status='Waiting for payment')
    context = {'documents':documents}
    return render(request, 'documents/pm/document_checked_pm.html', context)

def DocumentCheckView(request):
    if not request.user.is_authenticated:
        return redirect('login')
    if request.method == 'POST':
        id_document  = request.session['id_document'] 
        del request.session['id_document'] 
        Document.objects.filter(id=id_document).update(status='Waiting for payment')
        return redirect('document-checked')

    context={}
    return render(request, 'documents/pm/document_check.html', context)
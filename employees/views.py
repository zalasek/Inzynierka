from django.contrib.auth import authenticate, login, logout 
from django.shortcuts import redirect, render
from django.contrib.auth import login
from .models import Employee
from .forms import EmployeeForm
from django.contrib.auth.forms import UserCreationForm
from documents.models import Document

# Create your views here.

def LoginView(request):
    if request.user.is_authenticated:
        if request.user.employee.position == 'director':
            return redirect('director_home')
        if request.user.employee.position == 'project_menager':
            return redirect('project_menager_home')
        if request.user.employee.position == 'accounts':
            return redirect('accounts_home')
        else:
            return redirect('login')
        
    elif request.method == 'POST':
        username = request.POST.get('username') 
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)

        if user is not None:    
            login(request, user)
            if user.employee.position == 'director':
                return redirect('director_home')
            if user.employee.position == 'project_menager':
                return redirect('project_menager_home')
            if user.employee.position == 'accounts':
                return redirect('accounts_home')
        else:
            return redirect('login')
    else:
        context = {}
        return render(request, 'employees/login.html', context)

def LogoutView( request):
    logout(request)
    return redirect('login')

def EmployeeCreateView(request):
    if request.method == 'POST':
        form_user = UserCreationForm(request.POST)
        form_employee = EmployeeForm(request.POST)
        if form_user.is_valid() and form_employee.is_valid():
            
            user = form_user.save()

            employee = form_employee.save(commit=False) # nie zapisujemy odrazu
            employee.employee = user
            employee.save()
            username = form_user.cleaned_data.get('username')
            password = form_user.cleaned_data.get('password1')
            user = authenticate(username=username, password=password)
            login(request, user)
            return redirect('document-list')     
    else:
        form_user = UserCreationForm()
        form_employee = EmployeeForm()
    context = {'form_user': form_user, 'form_employee': form_employee}
    return render(request, 'employees/register.html', context)




def AccountsHomeView(request):
    if not request.user.is_authenticated:
            return redirect('login')
    else:
        if request.user.employee.position == 'accounts':
            documents_not_approved = Document.objects.filter(approved_director = False)
            documents_approved = Document.objects.filter(approved_director = True) 

            context = {'documents_not_approved':documents_not_approved,
                        'documents_approved':documents_approved,}            
            return render(request, 'employees/accounts_home.html', context)
        else:
            return redirect('login')



def ProjectMenagerHomeView(request):
    if not request.user.is_authenticated:
        return redirect('login')
    else:
        if request.user.employee.position == 'project_menager':
            context = {}
            return render(request, 'employees/project_menager_home.html', context)
        else:
            return redirect('login')



def DirectorHomeView(request):
    if not request.user.is_authenticated:
        return redirect('login')
    else:
        if request.user.employee.position == 'director':
            # products
            not_approved_director = Document.objects.filter(type = 'product').filter(approved_director = False).filter(approved_pm = True)
            not_approved_pm = Document.objects.filter(type = 'product').filter(approved_director = False).filter(approved_pm = False)

            context = {'not_approved_director':not_approved_director,
                        'not_approved_pm':not_approved_pm}

            return render(request, 'employees/director_home.html', context)
        else:
            return redirect('login')



        
        

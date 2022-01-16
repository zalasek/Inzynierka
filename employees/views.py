from django.contrib.auth import authenticate, login, logout 
from django.shortcuts import redirect, render
from django.contrib.auth import login
from .models import Employee
from .forms import EmployeeForm
from django.contrib.auth.forms import UserCreationForm
from documents.models import Document



############# LOGIN, LOGOUT, REGISTRATION #####################

def LoginView(request):
    if request.user.is_authenticated:
        if request.user.employee.position == 'director':
            return redirect('document-not-assigned')
        if request.user.employee.position == 'project_menager':
            return redirect('document-waiting-check')
        if request.user.employee.position == 'accounts':
            return redirect('document-list-waiting-payment')
        else:
            return redirect('login')  
    elif request.method == 'POST':
        username = request.POST.get('username') 
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:    
            login(request, user)
            if user.employee.position == 'director':
                return redirect('document-not-assigned')
            if user.employee.position == 'project_menager':
                return redirect('document-waiting-check')
            if user.employee.position == 'accounts':
                return redirect('document-list-waiting-payment')
        else:
            error = 'Wrong username or password!'
            context = {'error':error}
            return render(request, 'employees/login.html', context)
    else:
        context = {}
        return render(request, 'employees/login.html', context)

def LogoutView( request):
    logout(request)
    return redirect('login')








        
        

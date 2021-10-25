from django.contrib.auth import authenticate
from django.shortcuts import redirect, render
from django.contrib.auth import login
from .models import Employee
from .forms import EmployeeForm, ExtendedUserCreationForm # do edycji w razie potrzeby, (zamienic z UserCreationForm)
from django.contrib.auth.forms import UserCreationForm


# Create your views here.

def EmployeeCreateView(request):
    if request.method == 'POST':
        form_user = UserCreationForm(request.POST)
        form_employee = EmployeeForm(request.POST)
        if form_user.is_valid and form_employee.is_valid:
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
        
        

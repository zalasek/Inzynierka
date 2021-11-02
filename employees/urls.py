
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from .views import EmployeeCreateView, LoginView, LogoutView, AccountsHomeView, ProjectMenagerHomeView, DirectorHomeView


urlpatterns = [             
    path('register/', EmployeeCreateView, name='register'),
    path('login/', LoginView, name='login'),
    path('logout/', LogoutView, name='logout'),
    path('accounts_home/', AccountsHomeView, name='accounts_home'),
    path('director_home/', DirectorHomeView, name='director_home'),
    path('project_menager_home/', ProjectMenagerHomeView, name='project_menager_home'),
]





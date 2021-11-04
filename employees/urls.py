
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from .views import EmployeeCreateView, LoginView, LogoutView, ProjectMenagerHomeView, DirectorHomeView, AccountsHomeView


urlpatterns = [             
    path('register/', EmployeeCreateView, name='register'),
    path('login/', LoginView, name='login'),
    path('logout/', LogoutView, name='logout'),
    path('director/', LogoutView, name='director'),
    path('accounts/', LogoutView, name='accounts'),
    path('projectmenager/', LogoutView, name='projectmenager'),
]





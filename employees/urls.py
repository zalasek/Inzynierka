
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

<<<<<<< HEAD
from .views import EmployeeCreateView, LoginView, LogoutView, ProjectMenagerHomeView, DirectorHomeView, AccountsHomeView
=======
from .views import EmployeeCreateView, LoginView, LogoutView, AccountsHomeView, ProjectMenagerHomeView, DirectorHomeView
>>>>>>> 50d1113df6d65a0ec1fde7837d4c41f922645106


urlpatterns = [             
    path('register/', EmployeeCreateView, name='register'),
    path('login/', LoginView, name='login'),
    path('logout/', LogoutView, name='logout'),
<<<<<<< HEAD
    path('director/', LogoutView, name='director'),
    path('accounts/', LogoutView, name='accounts'),
    path('projectmenager/', LogoutView, name='projectmenager'),
=======
    path('accounts_home/', AccountsHomeView, name='accounts_home'),
    path('director_home/', DirectorHomeView, name='director_home'),
    path('project_menager_home/', ProjectMenagerHomeView, name='project_menager_home'),
>>>>>>> 50d1113df6d65a0ec1fde7837d4c41f922645106
]






from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from .views import  LoginView, LogoutView


urlpatterns = [         

### UNIVERSAL ###    

    path('login/', LoginView, name='login'),
    path('logout/', LogoutView, name='logout'),

]





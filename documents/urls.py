from django.urls import path
from .views import DocumentListView, DocumentDetailView

urlpatterns = [             
    path('documents/', DocumentListView, name='document-list'),
    path('document/<int:pk>', DocumentDetailView, name='document-detail'),
]
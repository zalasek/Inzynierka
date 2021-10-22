from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from .views import DocumentListView, DocumentDetailView, DocumentCreateView

urlpatterns = [             
    path('documents/', DocumentListView, name='document-list'),
    path('document/<int:pk>', DocumentDetailView, name='document-detail'),
    path('document-create', DocumentCreateView, name='document-create')
    
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
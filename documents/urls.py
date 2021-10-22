from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from .views import DocumentListView, DocumentDetailView, DocumentCreateView, DocumentDeleteView, DocumentUpdateView

urlpatterns = [             
    path('documents/', DocumentListView, name='document-list'),
    path('document/<int:pk>', DocumentDetailView, name='document-detail'),
    path('document-create', DocumentCreateView, name='document-create'),
    path('document-delete/<int:pk>', DocumentDeleteView, name='document-delete'),
    path('document-update/<int:pk>', DocumentUpdateView, name='document-update'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
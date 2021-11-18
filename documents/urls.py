from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from .views import DocumentListView, DocumentDetailView, DocumentCreateView, DocumentDeleteView, DocumentUpdateView, DocumentAssignView, DocumentCommentView

urlpatterns = [             
    path('', DocumentListView, name='document-list'),
    path('<int:pk>', DocumentDetailView, name='document-detail'),
    path('create', DocumentCreateView, name='document-create'),
    path('delete/<int:pk>', DocumentDeleteView, name='document-delete'),
    path('update/<int:pk>', DocumentUpdateView, name='document-update'),
    path('assign/<int:pk>', DocumentAssignView, name='document-assign'),
    path('comment/<int:pk>', DocumentCommentView, name='document-comment'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from .views import DocumentListAccountsView, DocumentDetailView, DocumentCreateAccountsView, DocumentDeleteAccountsView, DocumentUpdateAccountsView, DocumentAssignView, DocumentCommentView, DocumentApprovalView,DocumentListWaitingPaymentAccountsView,DocumentListFinishedAccountsView

urlpatterns = [           
    path('', DocumentListAccountsView, name='document-list'),
    path('finished/', DocumentListFinishedAccountsView, name='document-list-finished'),
    path('waiting-payment/', DocumentListWaitingPaymentAccountsView  , name='document-list-waiting-payment'),
    path('<int:pk>', DocumentDetailView, name='document-detail'),
    path('create', DocumentCreateAccountsView, name='document-create'),
    path('delete/<int:pk>', DocumentDeleteAccountsView, name='document-delete'),
    path('update/<int:pk>', DocumentUpdateAccountsView, name='document-update'),
    path('assign/<int:pk>', DocumentAssignView, name='document-assign'),
    path('comment/<int:pk>', DocumentCommentView, name='document-comment'),
    path('approval/<int:pk>', DocumentApprovalView, name='document-approval'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
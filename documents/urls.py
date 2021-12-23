from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from .views import DocumentListAccountsView, DocumentDetailView, DocumentCreateAccountsView, DocumentDeleteAccountsView, DocumentUpdateAccountsView, DocumentAssignView, DocumentCommentView, DocumentListWaitingApprovalView,DocumentListWaitingPaymentAccountsView,DocumentListFinishedAccountsView, DocumentListWaitingReturnDirectorView, DocumentListNotAssignedDirectorView, DocumentConfirmationApprovalView

urlpatterns = [     
    ## UNIVERSAL ##      
    path('<int:pk>', DocumentDetailView, name='document-detail'),
    path('comment/<int:pk>', DocumentCommentView, name='document-comment'),
    path('update/<int:pk>', DocumentUpdateAccountsView, name='document-update'),

    ## ACCOUNTS ##
    path('finished/', DocumentListFinishedAccountsView, name='document-list-finished'),
    path('waiting-payment/', DocumentListWaitingPaymentAccountsView  , name='document-list-waiting-payment'),
    path('', DocumentListAccountsView, name='document-list'),
    path('create', DocumentCreateAccountsView, name='document-create'),
    path('delete/<int:pk>', DocumentDeleteAccountsView, name='document-delete'),

    ## DIRECTOR  ##
    path('assign/<int:pk>', DocumentAssignView, name='document-assign'),
    path('waiting-approval/', DocumentListWaitingApprovalView, name='document-waiting-approval'),
    path('waiting-return/', DocumentListWaitingReturnDirectorView, name='document-waiting-return'),
    path('not-assigned/', DocumentListNotAssignedDirectorView, name='document-not-assigned'),
    path('confirm-approval/<int:pk>', DocumentConfirmationApprovalView, name='document-approval-confirmation'),

    ## PM ##




]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
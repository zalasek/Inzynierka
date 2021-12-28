from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from .views import DocumentListAccountsView, DocumentDetailAccountsView, DocumentCreateAccountsView, DocumentDeleteAccountsView, DocumentUpdateAccountsView, DocumentAssignView, DocumentCommentView, DocumentListWaitingApprovalView,DocumentListWaitingPaymentAccountsView,DocumentListFinishedAccountsView, DocumentListWaitingReturnDirectorView, DocumentListNotAssignedDirectorView, DocumentConfirmationApprovalView, DocumentApproveView, DocumentCheckedView, DocumentWaitingChecksView,DocumentCheckView, DocumentDetailDirectorView, DocumentDetailPmView, DocumentPaymentView

urlpatterns = [     
    ## UNIVERSAL ##      
    path('detail_accounts/<int:pk>', DocumentDetailAccountsView, name='document-detail-accounts'),
    path('comment/<int:pk>', DocumentCommentView, name='document-comment'),
    path('update/<int:pk>', DocumentUpdateAccountsView, name='document-update'),

    ## ACCOUNTS ##
    path('finished/', DocumentListFinishedAccountsView, name='document-list-finished'),
    path('waiting-payment/', DocumentListWaitingPaymentAccountsView  , name='document-list-waiting-payment'),
    path('', DocumentListAccountsView, name='document-list'),
    path('create', DocumentCreateAccountsView, name='document-create'),
    path('delete/<int:pk>', DocumentDeleteAccountsView, name='document-delete'),
    path('payment/', DocumentPaymentView, name='document-payment'),

    ## DIRECTOR  ##
    path('detail_director/<int:pk>', DocumentDetailDirectorView, name='document-detail-director'),
    path('assign/', DocumentAssignView, name='document-assign'),
    path('waiting-approval/', DocumentListWaitingApprovalView, name='document-waiting-approval'),
    path('waiting-return/', DocumentListWaitingReturnDirectorView, name='document-waiting-return'),
    path('not-assigned/', DocumentListNotAssignedDirectorView, name='document-not-assigned'),
    path('confirm-approval/<int:pk>', DocumentConfirmationApprovalView, name='document-approval-confirmation'),
    path('approve/', DocumentApproveView, name='document-approve'),

    ## PM ##
    path('detail_pm/<int:pk>', DocumentDetailPmView, name='document-detail-pm'), 
    path('checked/', DocumentCheckedView,  name='document-checked'),
    path('waiting-checks/', DocumentWaitingChecksView, name='document-waiting-check'),
    path('check/', DocumentCheckView, name='document-check'),


]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
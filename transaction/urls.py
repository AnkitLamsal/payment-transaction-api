from django.urls import path
from .views import TransactionListCreateView, TransactionDetailView, TransactionStatusUpdateView, GenerateAllTransactionPDFView, SingleTransactionPDFView
# from .views import index

urlpatterns = [
    path('transactions/', TransactionListCreateView.as_view(), name='transaction-create'),
    path('transactions/<str:transaction_id>/', TransactionDetailView.as_view(), name='transaction-detail'),
    path('transactions/<str:transaction_id>/status/', TransactionStatusUpdateView.as_view(), name='transaction-status-update'),
    path('pdf/transactions/', GenerateAllTransactionPDFView.as_view(), name='all-transactions-pdf'),
    path('pdf/transactions/<str:transaction_id>/', SingleTransactionPDFView.as_view(), name='single-transaction-pdf'),
    # path("", index, name="index"),
]
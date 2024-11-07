from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView, UpdateAPIView
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import TransactionSerializer, TransactionStatusSerializer
from rest_framework.permissions import IsAuthenticated
from .permissions import IsStaffUser, IsManager
from .models import Transaction
from django.http import JsonResponse, HttpResponse
from django.shortcuts import render
from django.template.loader import render_to_string
from django.conf import settings
from xhtml2pdf import pisa
from rest_framework.response import Response
from django.template.loader import get_template
import os
from io import BytesIO

class TransactionListCreateView(ListCreateAPIView):
    serializer_class = TransactionSerializer
    permission_classes = [IsStaffUser]
    queryset = Transaction.objects.all()
    lookup_field = 'transaction_id'

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        transaction = serializer.save()
        return Response({'transaction_id': transaction.transaction_id}, status=status.HTTP_201_CREATED)

class TransactionDetailView(RetrieveUpdateDestroyAPIView):
    queryset = Transaction.objects.all()
    serializer_class = TransactionSerializer
    lookup_field = 'transaction_id'
    permission_classes = [IsAuthenticated, ]

    def delete(self, request, *args, **kwargs):
        if not request.user.is_manager:
            return Response(status=status.HTTP_403_FORBIDDEN, data={'message': 'You are not allowed to perform this action'})
        else:
            return self.destroy(request, *args, **kwargs)

class TransactionStatusUpdateView(UpdateAPIView):
    queryset = Transaction.objects.all()
    serializer_class = TransactionStatusSerializer
    lookup_field = 'transaction_id'
    permission_classes = [IsManager]

class GenerateAllTransactionPDFView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        transactions = Transaction.objects.filter(transaction_status=True)
        html_content = render_to_string('transaction/all_transactions.html', {'transactions': transactions})
        pdf_path = os.path.join(settings.MEDIA_ROOT, 'transaction_report.pdf')
        with open(pdf_path, 'wb') as pdf_file:
            pisa_status = pisa.CreatePDF(BytesIO(html_content.encode('utf-8')), dest=pdf_file)
        if pisa_status.err:
            return JsonResponse({'error': 'PDF generation failed'}, status=500)
        pdf_url = request.build_absolute_uri(settings.MEDIA_URL + 'transaction_report.pdf')
        return JsonResponse({'pdf_url': pdf_url})

class SingleTransactionPDFView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, transaction_id, *args, **kwargs):
        try:
            transaction = Transaction.objects.get(transaction_id=transaction_id)
            if transaction.transaction_status == False:
                raise Transaction.DoesNotExist
        except Transaction.DoesNotExist:
            return Response({"error": "Transaction is not approved"}, status=404)

        html_content = render_to_string('transaction/specific_transactions.html', {'transaction': transaction})
        pdf_path = os.path.join(settings.MEDIA_ROOT, f'transaction_{transaction_id}_report.pdf')  
        with open(pdf_path, 'wb') as pdf_file:
            pisa_status = pisa.CreatePDF(
            BytesIO(html_content.encode('utf-8')), dest=pdf_file
            )
        if pisa_status.err:
            return JsonResponse({'error': 'PDF generation failed'}, status=500)
        pdf_url = request.build_absolute_uri(settings.MEDIA_URL + f'transaction_{transaction_id}_report.pdf')
        return JsonResponse({'pdf_url': pdf_url})
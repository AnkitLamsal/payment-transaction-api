# utils.py
from django.template.loader import render_to_string
from weasyprint import HTML
from django.http import HttpResponse
from .models import Transaction


def generate_pdf_for_all_transactions():
    transactions = Transaction.objects.filter(transaction_status=True)
    html_string = render_to_string('transaction/transactions_all.html', {'transactions': transactions})
    html = HTML(string=html_string)
    pdf = html.write_pdf()
    response = HttpResponse(pdf, content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="all_transactions.pdf"'
    return response

def generate_pdf_for_single_transaction(transaction_id):
    transaction = Transaction.objects.get(transaction_id=transaction_id, transaction_status=True)
    html_string = render_to_string('transaction/transaction_single.html', {'transaction': transaction})
    html = HTML(string=html_string)
    pdf = html.write_pdf()
    response = HttpResponse(pdf, content_type='application/pdf')
    response['Content-Disposition'] = f'attachment; filename="transaction_{transaction_id}.pdf"'
    return response
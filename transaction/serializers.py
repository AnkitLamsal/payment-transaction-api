from rest_framework import serializers
from .models import Transaction

class TransactionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Transaction
        fields = ['transaction_id', 'name', 'phone', 'email', 'amount', 'transaction_date']
        # read_only_fields = ['transaction_id']

class TransactionStatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = Transaction
        fields = ['transaction_id','transaction_status']


from django.db import models

class Transaction(models.Model):
    auto_increment_id = models.AutoField(primary_key=True)
    transaction_id = models.CharField(max_length=12, editable=False, unique=True)
    name = models.CharField(max_length=255)
    phone = models.CharField(max_length=20)
    email = models.EmailField()
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    transaction_date = models.DateTimeField()
    transaction_status = models.BooleanField(default=False)

    def save(self, *args, **kwargs):
        if not self.auto_increment_id:
            super(Transaction, self).save(*args, **kwargs)
            self.transaction_id = f'TXNID{self.auto_increment_id:04d}'
            Transaction.objects.filter(pk=self.pk).update(transaction_id=self.transaction_id)
        else:
            super(Transaction, self).save(*args, **kwargs)

    def __str__(self):
        return self.transaction_id

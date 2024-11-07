# Generated by Django 5.0.6 on 2024-11-07 12:07

from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Transaction",
            fields=[
                (
                    "auto_increment_id",
                    models.AutoField(primary_key=True, serialize=False),
                ),
                (
                    "transaction_id",
                    models.CharField(editable=False, max_length=12, unique=True),
                ),
                ("name", models.CharField(max_length=255)),
                ("phone", models.CharField(max_length=20)),
                ("email", models.EmailField(max_length=254)),
                ("amount", models.DecimalField(decimal_places=2, max_digits=10)),
                ("transaction_date", models.DateTimeField()),
            ],
        ),
    ]

# Generated by Django 5.0.2 on 2024-03-07 17:20

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("warehouse_app", "0006_alter_sale_selling_price"),
    ]

    operations = [
        migrations.AddField(
            model_name="sale",
            name="payment_type",
            field=models.CharField(
                choices=[("full", "Full Payment"), ("partial", "Partial Payment")],
                default="full",
                max_length=20,
            ),
        ),
        migrations.AddField(
            model_name="sale",
            name="remaining_due",
            field=models.DecimalField(decimal_places=2, default=0, max_digits=10),
        ),
    ]

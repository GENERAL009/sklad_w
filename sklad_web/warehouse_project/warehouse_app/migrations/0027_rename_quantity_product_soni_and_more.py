# Generated by Django 5.0.2 on 2024-03-17 20:15

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("warehouse_app", "0026_rename_name_product_nomi_alter_sale_payment_type"),
    ]

    operations = [
        migrations.RenameField(
            model_name="product",
            old_name="quantity",
            new_name="soni",
        ),
        migrations.RenameField(
            model_name="product",
            old_name="purchase_price",
            new_name="tan_narxi",
        ),
    ]

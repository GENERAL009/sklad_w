# Generated by Django 4.2.7 on 2024-03-18 03:57

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("warehouse_app", "0030_rename_sale_date_sale_sotilgan_sana_and_more"),
    ]

    operations = [
        migrations.RenameField(
            model_name="sale",
            old_name="sotilgan_soni",
            new_name="soni",
        ),
    ]

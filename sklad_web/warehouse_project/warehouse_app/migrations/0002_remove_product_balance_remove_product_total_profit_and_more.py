# Generated by Django 4.2.7 on 2024-02-28 18:07

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("warehouse_app", "0001_initial"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="product",
            name="balance",
        ),
        migrations.RemoveField(
            model_name="product",
            name="total_profit",
        ),
        migrations.RemoveField(
            model_name="sale",
            name="selling_price",
        ),
        migrations.AddField(
            model_name="product",
            name="phone_number",
            field=models.CharField(blank=True, max_length=15),
        ),
        migrations.AddField(
            model_name="product",
            name="selling_price",
            field=models.DecimalField(decimal_places=2, default=0, max_digits=10),
        ),
        migrations.AddField(
            model_name="product",
            name="total_given",
            field=models.DecimalField(decimal_places=2, default=0, max_digits=10),
        ),
        migrations.AddField(
            model_name="sale",
            name="phone_number",
            field=models.CharField(blank=True, max_length=15),
        ),
        migrations.AddField(
            model_name="sale",
            name="remaining_due",
            field=models.DecimalField(decimal_places=2, default=0, max_digits=10),
        ),
        migrations.AddField(
            model_name="sale",
            name="store",
            field=models.CharField(default="Default Store", max_length=255),
        ),
        migrations.AlterField(
            model_name="product",
            name="date_added",
            field=models.DateField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name="product",
            name="purchase_price",
            field=models.DecimalField(decimal_places=2, max_digits=10),
        ),
        migrations.AlterField(
            model_name="product",
            name="quantity",
            field=models.PositiveIntegerField(),
        ),
        migrations.AlterField(
            model_name="sale",
            name="profit",
            field=models.DecimalField(decimal_places=2, max_digits=10),
        ),
        migrations.AlterField(
            model_name="sale",
            name="quantity_sold",
            field=models.PositiveIntegerField(),
        ),
    ]

# Generated by Django 5.0.2 on 2024-03-09 05:31

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("warehouse_app", "0014_alter_profit_date"),
    ]

    operations = [
        migrations.AddField(
            model_name="profit",
            name="editable",
            field=models.BooleanField(default=True, editable=False),
        ),
        migrations.AlterField(
            model_name="profit",
            name="description",
            field=models.TextField(default="null", max_length=2),
        ),
    ]

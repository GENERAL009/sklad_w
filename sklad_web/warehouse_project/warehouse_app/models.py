from django.dispatch import receiver
from django.utils import timezone
from decimal import Decimal
from django.db.models.signals import post_save

from django.db import models
from django.db.models import Sum, Value, ExpressionWrapper, DecimalField, F
from django.db.models.functions import Coalesce


class Product(models.Model):
    nomi = models.CharField(max_length=255)
    date_added = models.DateField(auto_now_add=True)
    tan_narxi = models.DecimalField(max_digits=10, decimal_places=2)
    soni = models.PositiveIntegerField()

    def __str__(self):
        return self.nomi

class Sale(models.Model):
    name = models.CharField(max_length=255)
    mahsulot = models.ForeignKey(Product, on_delete=models.CASCADE,max_length=255)
    soni = models.PositiveIntegerField()
    sotilgan_sana = models.DateField()
    dokon = models.CharField(max_length=255)
    sotiladigan_narxi = models.DecimalField(max_digits=10, decimal_places=2)
    foyda = models.DecimalField(max_digits=10, decimal_places=2)
    tolash_usuli = models.CharField(max_length=20, choices=[('Naqd', 'Naqd'), ('Nasiya', 'Nasiya ')],default='full')
    qarz = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    is_paid = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.mahsulot.name} - {self.sotilgan_soni} sold on {self.sale_date}"



class Profit(models.Model):
    olinadigan_summa = models.DecimalField(max_digits=10, decimal_places=2)
    sana = models.DateField(default=timezone.now, editable=True)
    editable = models.BooleanField(default=True, editable=False)
    kommentariya = models.TextField(default="null")
    total_profit = models.DecimalField(max_digits=10, decimal_places=2, default=0)

    def __str__(self):
        return f"Profit - {self.amount} taken on {self.sana}"

    def save(self, *args, **kwargs):
        # Calculate total_sale_profit
        total_sale_profit = Sale.objects.aggregate(total_sale_profit=Sum('foyda'))['total_sale_profit'] or 0

        if self.total_profit is None:
            self.total_profit = total_sale_profit
        else:
            self.olinadigan_summa = self.olinadigan_summa or 0



        super().save(*args, **kwargs)

@receiver(post_save, sender=Sale)
def update_total_profit(sender, instance, **kwargs):
    total_sale_profit = Sale.objects.aggregate(total_sale_profit=Sum('foyda'))['total_sale_profit']
    if total_sale_profit is not None:
        profit = Profit.objects.last()
        olinadigan_summa = Profit.objects.aggregate(olinadigan_summa=Sum('olinadigan_summa'))['olinadigan_summa']
        if profit is not None:
            profit.total_profit = total_sale_profit - olinadigan_summa
            profit.save()
            
class PaymentUpdate(models.Model):
    sale = models.ForeignKey(Sale, on_delete=models.CASCADE)
    amount_paid = models.DecimalField(max_digits=10, decimal_places=2)
    payment_date = models.DateField(default=timezone.now)

    def __str__(self):
        return f"Payment for {self.sale.name} - {self.amount_paid} on {self.date}"


from django import forms
from .models import Product, Sale, Profit,PaymentUpdate

class ProductForm(forms.ModelForm):
    date_added = forms.DateField(widget=forms.HiddenInput(), required=False)

    class Meta:
        model = Product
        fields = ['nomi', 'tan_narxi', 'soni']

    def save(self, commit=True):
        nomi = self.cleaned_data['nomi']
        tan_narxi = self.cleaned_data['tan_narxi']
        soni = self.cleaned_data['soni']

        existing_product = Product.objects.filter(nomi=nomi).first()

        if existing_product:
            existing_product.soni += soni
            existing_product.tan_narxi = tan_narxi
            existing_product.save()
            return existing_product
        else:
            instance = super().save(commit=True)
            instance.date_added = Product.objects.get(pk=self.instance.pk).date_added
            if commit:
                instance.save()
            return instance


class SaleForm(forms.ModelForm):
    class Meta:
        model = Sale
        fields = ['mahsulot', 'soni', 'sotilgan_sana', 'dokon','sotiladigan_narxi','tolash_usuli']
        widgets = {
            'sotilgan_sana': forms.DateInput(attrs={'type': 'date'}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)


    def clean_sotilgan_soni(self):
        soni = self.cleaned_data['sotilgan_soni']
        product = self.cleaned_data['mahsulot']

        if soni > product.soni:
            raise forms.ValidationError('Maqsulot so`ralgan miqdordan kam')

        return soni
    def save(self, commit=True):
        sale = super().save(commit=False)

        products = sale.mahsulot
        tan_narxi = products.tan_narxi
        sale_price = sale.sotiladigan_narxi
        soni = sale.soni
        profit = (sale_price - tan_narxi) * soni

        products.soni -= soni
        products.save()


        sale.foyda = profit


        if commit:
            sale.save()

        return sale

class ProfitForm(forms.ModelForm):
    olinadigan_summa = forms.DecimalField(widget=forms.NumberInput(attrs={'required': 'required'}), initial=0)
    sana = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}))

    class Meta:
        model = Profit
        fields = ['olinadigan_summa', 'sana', 'kommentariya']

class PaymentUpdateForm(forms.ModelForm):
    class Meta:
        model = PaymentUpdate
        fields = ['amount_paid', 'payment_date']
        widgets = {
            'payment_date': forms.DateInput(attrs={'type': 'date'}),
        }

    def __init__(self, *args, **kwargs):
        super(PaymentUpdateForm, self).__init__(*args, **kwargs)
        self.fields['amount_paid'].label = 'Summa'
        self.fields['payment_date'].label = 'Sana'

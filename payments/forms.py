
from django import forms
from . import  models
from django.conf import settings

class InvoiceForm(forms.ModelForm):
    customer_nombre = forms.CharField(max_length=255)
    customer_apellido = forms.CharField(max_length=255)
    customer_segundo_apellido = forms.CharField(max_length=255)
    detalles = forms.Textarea()
    insurance = forms.ChoiceField(choices=settings.SEGUROS)
    items =forms.MultipleChoiceField(choices=settings.PRODUCTOS)

    class Meta:
        model = models.Invoice
        fields = ('customer_nombre','customer_apellido',
                  'customer_segundo_apellido','insurance','total','detalles','items')

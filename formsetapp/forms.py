from django.forms.models import inlineformset_factory

from django.forms import modelformset_factory
from django.forms import formset_factory
from django.forms import ModelForm, TextInput, HiddenInput, NumberInput
from django import forms
from formsetapp.models import *
from django.forms import ModelForm, TextInput, HiddenInput, NumberInput

class CustomerForm(forms.ModelForm):
    prefix = 'Customer'
    class Meta:
        model = Customer
        fields = '__all__'
  
OrderFormSet = inlineformset_factory(
    Customer, Order, extra=1,
    fields = '__all__',
    can_delete=True
    )
from .models import Income, Expense
from django import forms
from django.contrib.auth import get_user_model

User = get_user_model()

class IncomeForm(forms.ModelForm):
    class Meta:
        model = Income
        fields = ['amount', 'date', 'income_type', 'payment_method']
        widgets = {
            'date': forms.DateInput(attrs={'type': 'date'}),
        }

class ExpenseForm(forms.ModelForm):
    class Meta:
        model = Expense
        fields = ['amount', 'date', 'expense_type', 'payment_method']
        widgets = {
            'date': forms.DateInput(attrs={'type': 'date'}),
        }


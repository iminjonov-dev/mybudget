from .models import Income, Expense
from django.contrib import admin

@admin.register(Income)
class IncomeAdmin(admin.ModelAdmin):
    list_display = ('user', 'amount', 'income_type', 'payment_method', 'date')
    list_filter = ('income_type', 'payment_method', 'date')
    search_fields = ('user__username', 'income_type')


@admin.register(Expense)
class ExpenseAdmin(admin.ModelAdmin):
    list_display = ('user', 'amount', 'expense_type', 'payment_method', 'date')
    list_filter = ('expense_type', 'payment_method', 'date')
    search_fields = ('user__username', 'expense_type')



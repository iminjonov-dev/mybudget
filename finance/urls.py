from django.urls import path
from .views import IncomeListCreateView, ExpenseListCreateView, export_report, home_view, income_add_view, expense_add_view

urlpatterns = [
    path('', home_view, name='home'),
    path('income/add/', income_add_view, name='income_add'),
    path('expense/add/', expense_add_view, name='expense_add'),
    path('incomes/', IncomeListCreateView.as_view(), name='income-list-create'),
    path('expenses/', ExpenseListCreateView.as_view(), name='expense-list-create'),
    path('report/<str:period>/', export_report, name='export-report'),

]

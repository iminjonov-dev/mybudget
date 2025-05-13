from django.test import TestCase
from django.contrib.auth import get_user_model
from .models import Income
from datetime import date
from .models import Expense
from django.urls import reverse

User = get_user_model()

class IncomeModelTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='password123')
        self.income = Income.objects.create(
            user=self.user,
            amount=1000000,
            income_type='salary',
            payment_method='cash',
            date=date.today()
        )

    def test_income_created(self):
        self.assertEqual(self.income.amount, 1000000)
        self.assertEqual(self.income.income_type, 'salary')
        self.assertEqual(str(self.income), f"{self.user.username} - {self.income.amount} {self.income.income_type}")




class ExpenseModelTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser2', password='password123')
        self.expense = Expense.objects.create(
            user=self.user,
            amount=500000,
            expense_type='food',
            payment_method='card',
            date=date.today()
        )

    def test_expense_created(self):
        self.assertEqual(self.expense.amount, 500000)
        self.assertEqual(self.expense.expense_type, 'food')
        self.assertEqual(str(self.expense), f"{self.user.username} - {self.expense.amount} {self.expense.expense_type}")



class HomeViewTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='viewer', password='testpass123')
        self.client.login(username='viewer', password='testpass123')
        Income.objects.create(user=self.user, amount=200000, income_type='business', payment_method='cash', date=date.today())
        Expense.objects.create(user=self.user, amount=50000, expense_type='transport', payment_method='card', date=date.today())

    def test_home_view_status_code(self):
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Joriy Balans')

    def test_balance_calculation(self):
        response = self.client.get(reverse('home'))
        self.assertEqual(response.context['balance'], 150000)

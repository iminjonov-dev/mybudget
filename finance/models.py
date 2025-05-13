from django.conf import settings
from django.contrib.auth import get_user_model
from django.db import models

User = get_user_model()


class Income(models.Model):
    INCOME_TYPE_CHOICES = [
        ('salary', 'Oylik'),
        ('advance', 'Avans'),
        ('business', 'Biznes'),
    ]
    PAYMENT_METHOD_CHOICES = [
        ('cash', 'Naqd'),
        ('card', 'Karta'),
        ('currency', 'Valyuta'),
    ]

    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=12, decimal_places=2)
    income_type = models.CharField(max_length=10, choices=INCOME_TYPE_CHOICES)
    payment_method = models.CharField(max_length=10, choices=PAYMENT_METHOD_CHOICES)
    date = models.DateField()
    time = models.TimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} - {self.amount} {self.income_type}"

class Expense(models.Model):
    EXPENSE_TYPE_CHOICES = [
        ('transport', 'Yo‘l'),
        ('food', 'Oziq-ovqat'),
        ('tax', 'Soliq'),
        ('health', 'Sog‘liq'),
        ('entertainment', 'Ko‘ngil ochar'),
        ('other', 'Boshqa'),
    ]

    PAYMENT_METHOD_CHOICES = [
        ('cash', 'Naqd'),
        ('card', 'Karta'),
        ('currency', 'Valyuta'),
    ]

    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=12, decimal_places=2)
    expense_type = models.CharField(max_length=15, choices=EXPENSE_TYPE_CHOICES)
    payment_method = models.CharField(max_length=10, choices=PAYMENT_METHOD_CHOICES)
    date = models.DateField()
    time = models.TimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} - {self.amount} {self.expense_type}"




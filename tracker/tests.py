from django.test import TestCase
from .models import IncomeSource, ExpenseCategory, Transaction
from django.contrib.auth.models import User

class FinancialTrackingTests(TestCase):
    def setUp(self):
        # Create a test user
        self.user = User.objects.create_user(
            username='testuser',
            password='testpassword'
        )

        # Create test data for income sources, expense categories, and transactions
        self.income_source = IncomeSource.objects.create(name='Salary', amount=5000.00)
        self.expense_category = ExpenseCategory.objects.create(name='Groceries', total_spent=100.00)
        self.transaction = Transaction.objects.create(
            user=self.user,
            date='2023-01-15',
            amount=1000.00,
            description='Rent payment',
            source=self.income_source,
            category=self.expense_category
        )

    def test_income_source(self):
        income_source = IncomeSource.objects.get(name='Salary')
        self.assertEqual(income_source.amount, 5000.00)

    def test_expense_category(self):
        expense_category = ExpenseCategory.objects.get(name='Groceries')
        self.assertEqual(expense_category.total_spent, 100.00)

    def test_transaction(self):
        transaction = Transaction.objects.get(description='Rent payment')
        self.assertEqual(transaction.user, self.user)
        self.assertEqual(transaction.amount, 1000.00)

    def test_transaction_with_income_source(self):
        # Check if the transaction is associated with the correct income source
        self.assertEqual(self.transaction.source, self.income_source)

    def test_transaction_with_expense_category(self):
        # Check if the transaction is associated with the correct expense category
        self.assertEqual(self.transaction.category, self.expense_category)

    def test_transaction_with_user(self):
        # Check if the transaction is associated with the correct user
        self.assertEqual(self.transaction.user, self.user)

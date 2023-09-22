# from django import forms
# from .models import Category, Transaction

# class TransactionForm(forms.ModelForm):
#     category = forms.ModelChoiceField(
#         queryset=Category.objects.all(),
#         empty_label="Select an existing category",
#         required=False,  # Not required, as users can create new categories
#     )
#     new_category = forms.CharField(
#         max_length=100,
#         required=False,  # Not required, as users can select existing categories
#         label="Create a new category",
#     )

#     class Meta:
#         model = Transaction
#         fields = ['date', 'amount', 'description', 'type', 'category']
#         widgets = {
#             'date': forms.DateInput(attrs={'type': 'date'}),
#         }

from itertools import chain
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class CustomSignupForm(UserCreationForm):
    email = forms.EmailField(required=True)
    full_name = forms.CharField(max_length=100, required=True)

    class Meta:
        model = User
        fields = ['username', 'email', 'full_name', 'password1', 'password2']



# new
from django import forms
from .models import Income, Expenses

class IncomeForm(forms.ModelForm):
    class Meta:
        model = Income
        fields = ['income_category', 'income_amount', 'datetime', 'income_description']
    receipt = forms.ImageField(required=False)

class ExpensesForm(forms.ModelForm):
    class Meta:
        model = Expenses
        fields = ['expense_category', 'expenses_amount', 'datetime', 'expenses_description']
    receipt = forms.ImageField(required=False)


from django import forms
from .models import BudgetGoal

class BudgetGoalForm(forms.ModelForm):
    class Meta:
        model = BudgetGoal
        fields = ['expense_category', 'goal_amount', 'duration']


from django import forms
from .models import SharedExpense

class SharedExpenseForm(forms.ModelForm):
    class Meta:
        model = SharedExpense
        fields = ['payer', 'amount', 'date', 'description', 'participants']


from django import forms

class ContactForm(forms.Form):
    name = forms.CharField(max_length=100)
    email = forms.EmailField()
    subject = forms.CharField(max_length=200)
    message = forms.CharField(widget=forms.Textarea)



# class SettlementForm(forms.ModelForm):
#     class Meta:
#         model = SharedExpense
#         fields = ['amount_paid']



#reciept upload form 

# from django import forms
# from .models import Receipt, Income, Expenses
# from itertools import chain

# class ReceiptUploadForm(forms.ModelForm):
#     class Meta:
#         model = Receipt
#         fields = ['receipt_image']

#     transaction_category = forms.ModelChoiceField(queryset=Income.objects.none(), required=False, label='Transactions')

#     def __init__(self, *args, **kwargs):
#         super().__init__(*args, **kwargs)
        
#         # Access the 'uploaded_by' user from the form's instance
#         uploaded_by = self.instance.uploaded_by if self.instance else None
        
#         # Fetch income and expenses for the user
#         income_list = Income.objects.filter(user=uploaded_by)
#         expenses_list = Expenses.objects.filter(user=uploaded_by)

#         # Combine and sort transactions by date
#         transactions = sorted(chain(income_list, expenses_list), key=lambda transaction: transaction.datetime, reverse=True)

#         # Set the queryset for the 'transaction_category' field
#         self.fields['transaction_category'].queryset = transactions

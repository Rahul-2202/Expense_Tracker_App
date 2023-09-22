# from django.db import models
# from django.contrib.auth.models import User

#old db structure


# class Category(models.Model):
#     CATEGORY_CHOICES = [
#         ('+', 'Income'),
#         ('-', 'Expense'),
#     ]
#     name = models.CharField(max_length=100)
#     type = models.CharField(max_length=1, choices=CATEGORY_CHOICES,default="-")
#     total_amount = models.DecimalField(max_digits=10, decimal_places=2, default=0)

#     def __str__(self):
#         return self.name    

# class Transaction(models.Model):
#     user = models.ForeignKey(User, on_delete=models.CASCADE)  # Link to the User model
#     date = models.DateField()
#     amount = models.DecimalField(max_digits=10, decimal_places=2)
#     description = models.TextField()
#     type = models.CharField(max_length=1, choices=[('+', 'Income'), ('-', 'Expense')],default="-")
#     category = models.ForeignKey(Category, on_delete=models.CASCADE, null=True, blank=True)

#     def __str__(self):
#         return f"Transaction on {self.date}: {self.description}"


#################################################################################################################

#reciept uploadinf





from django.db import models
from django.contrib.auth.models import User

# User model for authentication
# You can extend the built-in User model or use it directly
# Here, we are extending it to include full_name and email fields
# class UserProfile(models.Model):
#     user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
#     full_name = models.CharField(max_length=255)
#     email = models.EmailField()


from django.db import models
from django.contrib.auth.models import User

# class Receipt(models.Model):
#     uploaded_by = models.ForeignKey(User, on_delete=models.CASCADE)
#     upload_date = models.DateTimeField(auto_now_add=True)
#     receipt_image = models.ImageField(upload_to='receipts/')
#     income_transactions = models.ManyToManyField('Income', related_name='receipts', blank=True)
#     expenses_transactions = models.ManyToManyField('Expenses', related_name='receipts', blank=True)

#     def __str__(self):
#         return f'Receipt {self.id} uploaded by {self.uploaded_by}'


# Model for Income
class Income(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    income_category = models.CharField(max_length=255)
    income_amount = models.DecimalField(max_digits=10, decimal_places=2)
    datetime = models.DateTimeField()
    income_description = models.TextField()
    receipt = models.ImageField(upload_to='income_receipts/', blank=True, null=True)

# Model for Expenses
class Expenses(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    expense_category = models.CharField(max_length=255)
    expenses_amount = models.DecimalField(max_digits=10, decimal_places=2)
    datetime = models.DateTimeField()
    expenses_description = models.TextField()
    receipt = models.ImageField(upload_to='expense_receipts/', blank=True, null=True) 


#setting budget goals
from django.db import models
from django.contrib.auth.models import User

class BudgetGoal(models.Model):
    DURATION_CHOICES = (
        ('weekly', 'Weekly'),
        ('monthly', 'Monthly'),
        ('yearly', 'Yearly'),
    )
    
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    expense_category = models.CharField(max_length=255)
    goal_amount = models.DecimalField(max_digits=10, decimal_places=2)
    duration = models.CharField(max_length=10, choices=DURATION_CHOICES)


#shared expenses

from django.db import models
from django.contrib.auth.models import User

class SharedExpense(models.Model):
    payer = models.ForeignKey(User, on_delete=models.CASCADE, related_name='paid_expenses')
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    date = models.DateField()
    description = models.TextField()
    
    participants = models.ManyToManyField(User, related_name='shared_expenses')

    def calculate_share(self):
        # Calculate how much each participant owes for this shared expense
        total_participants = self.participants.count()
        share_per_participant = self.amount / total_participants
        return share_per_participant




# contactform/models.py

from django.db import models

class ContactSubmission(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    subject = models.CharField(max_length=200)
    message = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.subject

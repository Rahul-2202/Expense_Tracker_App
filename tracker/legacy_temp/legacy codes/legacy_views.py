

# # from django.shortcuts import render
# # from .models import Transaction
# # from django.db import models

# # def transaction_list(request):
# #     transactions = Transaction.objects.filter(user=request.user)

# #     # Calculate total income and total expenses
# #     total_income = transactions.filter(source__isnull=False).aggregate(total=models.Sum('amount'))['total'] or 0
# #     total_expenses = transactions.filter(category__isnull=False).aggregate(total=models.Sum('amount'))['total'] or 0

# #     return render(request, 'tracker/transactions.html', {
# #         'transactions': transactions,
# #         'total_income': total_income,
# #         'total_expenses': total_expenses,
# #     })



# from django.shortcuts import render, redirect, get_object_or_404
# from django.contrib.auth.decorators import login_required
# from .models import Category, Transaction
# from .forms import TransactionForm  # Create a TransactionForm for adding/editing transactions
# # @login_required 
# # def add_transaction(request):
# #     if request.method == 'POST':
# #         form = TransactionForm(request.POST)
# #         if form.is_valid():
# #             transaction = form.save(commit=False)
# #             transaction.user = request.user  # Assign the current user to the transaction
# #             transaction.save()
# #             return redirect('transaction_list')
# #     else:
# #         form = TransactionForm()
# #     return render(request, 'tracker/add_transaction.html', {'form': form})


# # @login_required 
# # def edit_transaction(request, transaction_id):
# #     transaction = get_object_or_404(Transaction, pk=transaction_id)
# #     if request.method == 'POST':
# #         form = TransactionForm(request.POST, instance=transaction)
# #         if form.is_valid():
# #             form.save()
# #             return redirect('transaction_list')
# #     else:
# #         form = TransactionForm(instance=transaction)
# #     return render(request, 'tracker/edit_transaction.html', {'form': form, 'transaction': transaction})


# # @login_required 
# # def delete_transaction(request, transaction_id):
# #     transaction = get_object_or_404(Transaction, pk=transaction_id)
# #     if request.method == 'POST':
# #         transaction.delete()
# #         return redirect('transaction_list')
# #     return render(request, 'tracker/delete_transaction.html', {'transaction': transaction})

# # @login_required 
# # def transaction_list(request):
# #     transactions = Transaction.objects.filter(user=request.user)
# #     return render(request, 'tracker/transaction_list.html', {'transactions': transactions})

# from django.shortcuts import render, redirect, get_object_or_404
# from django.contrib.auth.decorators import login_required
# from .models import Transaction
# from .forms import TransactionForm
# from django.db import models

# @login_required
# def transaction_list(request):
#     transactions = Transaction.objects.filter(user=request.user)
#     total_income = Transaction.objects.filter(user=request.user, type='+').aggregate(total=models.Sum('amount'))['total']
#     total_expense = Transaction.objects.filter(user=request.user, type='-').aggregate(total=models.Sum('amount'))['total']
#     return render(request, 'tracker/transaction_list.html', {
#         'transactions': transactions,
#         'total_income': total_income or 0,
#         'total_expense': total_expense or 0,
#     })

# @login_required
# def add_transaction(request):
#     if request.method == 'POST':
#         form = TransactionForm(request.POST)
#         if form.is_valid():
#             transaction = form.save(commit=False)
#             transaction.user = request.user  # Assign the current user to the transaction
#             transaction.save()
#             return redirect('transaction_list')
#     else:
#         form = TransactionForm()
#     return render(request, 'tracker/add_transaction.html', {'form': form})

# @login_required
# def edit_transaction(request, transaction_id):
#     transaction = get_object_or_404(Transaction, pk=transaction_id, user=request.user)
#     if request.method == 'POST':
#         form = TransactionForm(request.POST, instance=transaction)
#         if form.is_valid():
#             form.save()
#             return redirect('transaction_list')
#     else:
#         form = TransactionForm(instance=transaction)
#     return render(request, 'tracker/edit_transaction.html', {'form': form, 'transaction': transaction})

# @login_required
# def delete_transaction(request, transaction_id):
#     transaction = get_object_or_404(Transaction, pk=transaction_id, user=request.user)
#     if request.method == 'POST':
#         transaction.delete()
#         return redirect('transaction_list')
#     return render(request, 'tracker/delete_transaction.html', {'transaction': transaction})


# from django.contrib.auth.models import User
# from tracker.models import Transaction
# import random
# from datetime import datetime, timedelta
# from decimal import Decimal

# def sampler_transaction(request):
#     sample_transaction_descriptions = [
#         'Salary', 'Groceries', 'Rent', 'Dinner out', 'Electricity bill',
#         'Freelance income', 'Movie tickets', 'Phone bill', 'Gas bill', 'Internet bill',
#         'Clothing', 'Car payment', 'Health insurance', 'Vacation', 'Gym membership',
#     ]

#     sample_transactions = []

#     # Generate 100 sample transactions
#     for _ in range(100):
#         random_date = datetime.now() - timedelta(days=random.randint(1, 90))  # Random date within the last 3 months
#         random_amount = Decimal(random.uniform(10, 500))  # Random amount between 10 and 500
#         random_description = random.choice(sample_transaction_descriptions)
#         transaction_type = '+' if random.randint(0, 1) == 0 else '-'  # Randomly choose income or expense

#         transaction_data = {
#             'date': random_date.strftime('%Y-%m-%d'),
#             'amount': random_amount,
#             'description': random_description,
#             'type': transaction_type,
#         }

#         sample_transactions.append(transaction_data)

#     # Now, you have a list of 100 sample transactions with random dates within a 3-month duration.


#     for transaction_data in sample_transactions:
#         Transaction.objects.create(
#             user=User.objects.get(username=request.user),
#             date=transaction_data['date'],
#             amount=transaction_data['amount'],
#             description=transaction_data['description'],
#             type=transaction_data['type'],
#         )

#     return render(request, "tracker/sampler.html")


# import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# def graphs(request):
#     # Load data or create DataFrames for your graphs here
#     # Example data:
#     transactions_df = Transaction.objects.filter(user=request.user)
#     # transactions_df = pd.DataFrame(...)  # Your transaction data
#     expenses_by_category_df = Category.objects.all()  # Your expense category data

#     # Generate the individual graphs
#     fig, axes = plt.subplots(nrows=2, ncols=2, figsize=(12, 8))

#     # Graph 1: Line Plot (Time Series)
#     income_df = transactions_df[transactions_df['type'] == '+']
#     expense_df = transactions_df[transactions_df['type'] == '-']
#     axes[0, 0].plot(income_df['date'], income_df['amount'], label='Income', marker='o')
#     axes[0, 0].plot(expense_df['date'], expense_df['amount'], label='Expenses', marker='o')
#     axes[0, 0].set_xlabel('Date')
#     axes[0, 0].set_ylabel('Amount')
#     axes[0, 0].set_title('Income vs. Expenses Over Time')
#     axes[0, 0].legend()
#     axes[0, 0].grid()

#     # Graph 2: Bar Plot (Category Analysis)
#     sns.barplot(x='total_amount', y='category', data=expenses_by_category_df, ax=axes[0, 1])
#     axes[0, 1].set_xlabel('Total Amount')
#     axes[0, 1].set_ylabel('Expense Category')
#     axes[0, 1].set_title('Expenses by Category')
#     axes[0, 1].grid()

#     # Graph 3: Pie Chart (Category Distribution)
#     labels = expenses_by_category_df['category']
#     sizes = expenses_by_category_df['total_amount']
#     axes[1, 0].pie(sizes, labels=labels, autopct='%1.1f%%')
#     axes[1, 0].set_title('Expense Category Distribution')

#     # Graph 4: Histogram (Expense Distribution)
#     axes[1, 1].hist(transactions_df[transactions_df['type'] == '-']['amount'], bins=20, edgecolor='k')
#     axes[1, 1].set_xlabel('Expense Amount')
#     axes[1, 1].set_ylabel('Frequency')
#     axes[1, 1].set_title('Expense Distribution')
#     axes[1, 1].grid()

#     # Save the figure with all graphs
#     plt.tight_layout()  # Ensure proper layout
#     plt.savefig('path_to_save_plot.png')  # Modify this to save the plot to a file
#     plt.close()  # Close the plot to free up resources

#     # Optionally, return the saved plot as an image in the HTTP response
#     with open('path_to_save_plot.png', 'rb') as img_file:
#         response = HttpResponse(content_type='image/png')
#         response.write(img_file.read())

#     return response

from django.contrib.auth.models import User
from tracker.models import Transaction


import random
from datetime import datetime, timedelta
from decimal import Decimal

# Sample transaction data
sample_transaction_descriptions = [
    'Salary', 'Groceries', 'Rent', 'Dinner out', 'Electricity bill',
    'Freelance income', 'Movie tickets', 'Phone bill', 'Gas bill', 'Internet bill',
    'Clothing', 'Car payment', 'Health insurance', 'Vacation', 'Gym membership',
]

sample_transactions = []

# Generate 100 sample transactions
for _ in range(100):
    random_date = datetime.now() - timedelta(days=random.randint(1, 90))  # Random date within the last 3 months
    random_amount = Decimal(random.uniform(10, 500))  # Random amount between 10 and 500
    random_description = random.choice(sample_transaction_descriptions)
    transaction_type = '+' if random.randint(0, 1) == 0 else '-'  # Randomly choose income or expense

    transaction_data = {
        'date': random_date.strftime('%Y-%m-%d'),
        'amount': random_amount,
        'description': random_description,
        'type': transaction_type,
    }

    sample_transactions.append(transaction_data)

# Now, you have a list of 100 sample transactions with random dates within a 3-month duration.



# sample_transactions = [
#     {'date': '2023-09-15', 'amount': 100.00, 'description': 'Salary', 'type': '+'},
#     {'date': '2023-09-16', 'amount': 50.00, 'description': 'Groceries', 'type': '-'},
#     {'date': '2023-09-18', 'amount': 200.00, 'description': 'Rent', 'type': '-'},
# ]

for transaction_data in sample_transactions:
    Transaction.objects.create(
        user=User.objects.get(username='Rahul'),
        date=transaction_data['date'],
        amount=transaction_data['amount'],
        description=transaction_data['description'],
        type=transaction_data['type'],
    )
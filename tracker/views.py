from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.shortcuts import render, redirect
from django.contrib.auth.models import User


# # Create your views here.
# from django.http import HttpResponse


def home(request):
    return render(request, "tracker/home.html")



from .forms import CustomSignupForm

def signup(request):
    if request.method == 'POST':
        form = CustomSignupForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)  
            return redirect("home") 
    else:
        form = CustomSignupForm()
    return render(request, 'tracker/pages/signup_new.html', {'form': form})


from django.contrib.auth.models import User

def print_all_users(request):
    # Retrieve all user objects from the database
    all_users = User.objects.all()

    return render(request, 'tracker/Users.html', {'all_users': all_users})


# new

from django.shortcuts import render, redirect
from .models import ContactSubmission, Income, Expenses
from .forms import IncomeForm, ExpensesForm
from django.contrib.auth.decorators import login_required
def add_income(request):
    if request.method == 'POST':
        form = IncomeForm(request.POST, request.FILES)
        if form.is_valid():
            income = form.save(commit=False)
            income.user = request.user 
            income.save()
            return redirect('transactions')  # Redirect to a home or any other relevant page
    else:
        form = IncomeForm()
    
    return render(request, 'tracker/add_income.html', {'form': form})

def add_expense(request):
    if request.method == 'POST':
        form = ExpensesForm(request.POST, request.FILES)
        if form.is_valid():
            expense = form.save(commit=False)
            expense.user = request.user 
            expense.save()
            return redirect('transactions')  # Redirect to a home or any other relevant page
    else:
        form = ExpensesForm()
    
    return render(request, 'tracker/add_expense.html', {'form': form})

def delete_income(request, income_id):
    income = get_object_or_404(Income, pk=income_id)
    
    if request.method == 'POST':
        income.delete()
        return redirect('transactions')  # Redirect to a home or any other relevant page
    
    return render(request, 'tracker/delete_income.html', {'income': income})

from django.shortcuts import render, redirect, get_object_or_404
from .models import Income
from .forms import IncomeForm

def edit_income(request, income_id):
    income = get_object_or_404(Income, pk=income_id)
    
    if request.method == 'POST':
        form = IncomeForm(request.POST, instance=income)
        if form.is_valid():
            form.save()
            return redirect('transactions')  # Redirect to a home or any other relevant page
    else:
        form = IncomeForm(instance=income)
    
    return render(request, 'tracker/edit_income.html', {'form': form, 'income': income})


from django.shortcuts import render, redirect, get_object_or_404
from .models import Expenses

def delete_expense(request, expense_id):
    expense = get_object_or_404(Expenses, pk=expense_id)
    
    if request.method == 'POST':
        expense.delete()
        return redirect('transactions')  # Redirect to a home or any other relevant page
    
    return render(request, 'tracker/delete_expense.html', {'expense': expense})


from django.shortcuts import render, redirect, get_object_or_404
from .models import Expenses
from .forms import ExpensesForm

def edit_expense(request, expense_id):
    expense = get_object_or_404(Expenses, pk=expense_id)
    
    if request.method == 'POST':
        form = ExpensesForm(request.POST, instance=expense)
        if form.is_valid():
            form.save()
            return redirect('transactions')  # Redirect to a home or any other relevant page
    else:
        form = ExpensesForm(instance=expense)
    
    return render(request, 'tracker/edit_expense.html', {'form': form, 'expense': expense})


from django.shortcuts import render
from .models import Income, Expenses

def income_expenses_list(request):
    # Get the income and expenses for the logged-in user
    user_profile = request.user  # Assuming you're using the UserProfile model as mentioned before
    income_list = Income.objects.filter(user=user_profile)
    expenses_list = Expenses.objects.filter(user=user_profile)

    return render(request, 'tracker/income_expenses_list.html', {'income_list': income_list, 'expenses_list': expenses_list})



from django.shortcuts import render
from .models import Income, Expenses
from itertools import chain

@login_required
def transaction_list(request):
    # Get the income and expenses for the logged-in user
    user_profile = request.user
    income_list = Income.objects.filter(user=user_profile)
    expenses_list = Expenses.objects.filter(user=user_profile)

    # Combine and sort transactions by date
    transactions = sorted(chain(income_list, expenses_list), key=lambda transaction: transaction.datetime, reverse=True)

    return render(request, 'tracker/pages/transaction_page.html', {'transactions': transactions})



# from django.shortcuts import render, redirect
# from django.db.models import Sum
# from .models import Expenses, BudgetGoal
# from .forms import BudgetGoalForm

# def budget_view(request):
    user_profile = request.user
    expenses = Expenses.objects.filter(user=user_profile)
    
    if request.method == 'POST':
        form = BudgetGoalForm(request.POST)
        if form.is_valid():
            budget_goal = form.save(commit=False)
            budget_goal.user = user_profile
            budget_goal.save()
            return redirect('budget')  # Redirect back to the budget page after setting a goal

    form = BudgetGoalForm()
    
    # Calculate total expenses for tracking overall budget
    total_expenses = sum(expense.expenses_amount for expense in expenses)
    
    # Fetch budget goals for the user
    budget_goals = BudgetGoal.objects.filter(user=user_profile)
    
    # Calculate and display progress for each goal
    for goal in budget_goals:
        goal.total_expenses = expenses.filter(expense_category=goal.expense_category).aggregate(Sum('expenses_amount'))['expenses_amount__sum'] or 0
        goal.progress = (goal.total_expenses / goal.goal_amount) * 100 if goal.goal_amount > 0 else 0

    return render(request, 'tracker/budget.html', {'expenses': expenses, 'total_expenses': total_expenses, 'form': form, 'budget_goals': budget_goals})

from django.core.mail import send_mail
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.db.models import Sum
from .models import Expenses, BudgetGoal
from .forms import BudgetGoalForm

def budget_view(request):
    user_profile = request.user
    expenses = Expenses.objects.filter(user=user_profile)
    
    if request.method == 'POST':
        form = BudgetGoalForm(request.POST)
        if form.is_valid():
            budget_goal = form.save(commit=False)
            budget_goal.user = user_profile
            budget_goal.save()
            return redirect('budget')  # Redirect back to the budget page after setting a goal

    form = BudgetGoalForm()
    
    # Calculate total expenses for tracking overall budget
    total_expenses = sum(expense.expenses_amount for expense in expenses)
    
    # Fetch budget goals for the user
    budget_goals = BudgetGoal.objects.filter(user=user_profile)
    
    # Calculate and display progress for each goal
    for goal in budget_goals:
        goal.total_expenses = expenses.filter(expense_category=goal.expense_category).aggregate(Sum('expenses_amount'))['expenses_amount__sum'] or 0
        goal.progress = (goal.total_expenses / goal.goal_amount) * 100 if goal.goal_amount > 0 else 0

        # Check if expenses exceed the goal and send an email
        if goal.total_expenses > goal.goal_amount:
            subject = f'Budget Exceeded for {goal.expense_category}'
            message = f'Your budget for {goal.expense_category} has been exceeded.'
            from_email = 'rahulmanglani0@gmail.com'  # Replace with your sender email
            recipient_list = [user_profile.email]  # List of recipient email addresses

            send_mail(subject, message, from_email, recipient_list)

    return render(request, 'tracker/budget.html', {'expenses': expenses, 'total_expenses': total_expenses, 'form': form, 'budget_goals': budget_goals})


from django.shortcuts import render, redirect, get_object_or_404
from .models import BudgetGoal
from .forms import BudgetGoalForm  # Ensure you have the BudgetGoalForm defined in forms.py

def edit_budget_goal(request, goal_id):
    user_profile = request.user
    goal = get_object_or_404(BudgetGoal, id=goal_id, user=user_profile)

    if request.method == 'POST':
        form = BudgetGoalForm(request.POST, instance=goal)
        if form.is_valid():
            form.save()
            return redirect('budget')  # Redirect back to the budget page

    else:
        form = BudgetGoalForm(instance=goal)

    return render(request, 'tracker/edit_budget_goal.html', {'form': form})

from django.shortcuts import render, redirect, get_object_or_404
from .models import BudgetGoal

def delete_budget_goal(request, goal_id):
    user_profile = request.user
    goal = get_object_or_404(BudgetGoal, id=goal_id, user=user_profile)

    if request.method == 'POST':
        goal.delete()
        return redirect('budget')  # Redirect back to the budget page

    return redirect('budget')




from django.shortcuts import render
from django.db.models import Sum
from datetime import date, timedelta
from .models import Income, Expenses

def financial_report(request):
    user_profile = request.user
    end_date = date.today()
    start_date = end_date - timedelta(days=365)  # 12 months ago

    # Query income and expenses for the past 12 months
    income_data = Income.objects.filter(
        user=user_profile, datetime__range=(start_date, end_date)
    ).values('datetime__month').annotate(total_income=Sum('income_amount')).order_by('datetime__month')

    expenses_data = Expenses.objects.filter(
        user=user_profile, datetime__range=(start_date, end_date)
    ).values('datetime__month').annotate(total_expenses=Sum('expenses_amount')).order_by('datetime__month')

    # Calculate monthly savings and major expense category
    financial_data = []
    for month in range(1, 13):
        income = income_data.filter(datetime__month=month).first()
        expenses = expenses_data.filter(datetime__month=month).first()
        
        if income is None:
            income_amount = 0
        else:
            income_amount = income['total_income']
        
        if expenses is None:
            expenses_amount = 0
            major_expense_category = "No Expenses"
        else:
            expenses_amount = expenses['total_expenses']
            major_expense = Expenses.objects.filter(
                user=user_profile, datetime__month=month
            ).values('expense_category').annotate(total=Sum('expenses_amount')).order_by('-total').first()
            major_expense_category = major_expense['expense_category'] if major_expense else "No Expenses"

        savings = income_amount - expenses_amount
        financial_data.append({
            'month': month,
            'total_income': income_amount,
            'total_expenses': expenses_amount,
            'savings': savings,
            'major_expense_category': major_expense_category,
        })

    return render(request, 'tracker/financial_report.html', {'financial_data': financial_data})



# shared expenses

from django.shortcuts import render, redirect
from .models import SharedExpense
from .forms import SharedExpenseForm

def create_shared_expense(request):
    if request.method == 'POST':
        form = SharedExpenseForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('list_shared_expenses')
    else:
        form = SharedExpenseForm()
    
    return render(request, 'tracker/create_shared_expense.html', {'form': form})


from django.shortcuts import render
from .models import SharedExpense

def list_shared_expenses(request):
    shared_expenses = SharedExpense.objects.filter(payer=request.user)
    return render(request, 'tracker/list_shared_expenses.html', {'shared_expenses': shared_expenses})


# from django.shortcuts import render, redirect, get_object_or_404
# from .models import SharedExpense
# from .forms import SettlementForm

# def settle_shared_expense(request, expense_id):
#     expense = get_object_or_404(SharedExpense, id=expense_id)
    
#     if request.method == 'POST':
#         form = SettlementForm(request.POST, instance=expense)
#         if form.is_valid():
#             form.save()
#             return redirect('list_shared_expenses')
#     else:
#         form = SettlementForm(instance=expense)
    
#     return render(request, 'tracker/settle_shared_expense.html', {'form': form, 'expense': expense})

from django.shortcuts import render
from .models import SharedExpense

def debt_status(request):
    user = request.user

    # Calculate the total amount shared by the user
    total_shared_amount = 0

    # Calculate the total amount others owe to the user
    total_amount_others_owe_payer = 0

    # Get all shared expenses where the user is the payer
    payer_shared_expenses = SharedExpense.objects.filter(payer=user)

    for expense in payer_shared_expenses:
        total_shared_amount += expense.amount

    # Get all shared expenses where the user is a participant
    user_shared_expenses = SharedExpense.objects.filter(participants=user)

    for expense in user_shared_expenses:
        total_participants = expense.participants.count() + 1  # Include the payer
        user_share = expense.amount / total_participants
        total_amount_others_owe_payer += user_share

    return render(request, 'tracker/debt_shared_status.html', {
        'total_shared_amount': total_shared_amount,
        'total_amount_others_owe_payer': total_amount_others_owe_payer
    })



# receipt uploadinhg


# from django.shortcuts import render, redirect

# def upload_receipt(request):
#     if request.method == 'POST':
#         form = ReceiptUploadForm(request.POST, request.FILES)
#         if form.is_valid():
#             receipt = form.save(commit=False)
#             receipt.uploaded_by = request.user  # Set the uploaded_by field
#             receipt.save()
#             return redirect('receipt_detail', receipt_id=receipt.id)
#     else:
#         form = ReceiptUploadForm()
    
#     return render(request, 'tracker/upload_receipt.html', {'form': form})



# from django.shortcuts import render, get_object_or_404
# from .models import Receipt

# def receipt_detail(request, receipt_id):
#     receipt = get_object_or_404(Receipt, pk=receipt_id)
#     return render(request, 'tracker/receipt_detail.html', {'receipt': receipt})


# from django.shortcuts import render
# from .models import Receipt

# def receipt_list(request):
#     receipts = Receipt.objects.all()
#     return render(request, 'tracker/receipt_list.html', {'receipts': receipts})



# send email

# import requests
# from django.http import JsonResponse


# from django.core.mail import send_mail
# from django.http import HttpResponse
# from django.conf import settings

# def send_email(request):
#     subject = 'Test Email'
#     message = 'This is a test email sent from Django.'
#     from_email = 'rahulmanglani0@gmail.com'
#     recipient_list = request.user.email  # List of recipient email addresses

#     send_mail(subject, message, from_email, recipient_list)

#     return HttpResponse('Test email sent!')


#dashboard



from django.shortcuts import render
from django.db.models import Sum
from .models import Income, Expenses, BudgetGoal
from django.contrib.auth.models import User
from itertools import chain
import json
from datetime import datetime, timedelta
from .custom_json_encoder import CustomJSONEncoder

@login_required
def dashboard(request):
    user_profile = request.user

    # Get the top five latest transactions
    transactions = get_latest_transactions(user_profile, 5)

    # Get total income and total expenses
    total_income = get_total_income(user_profile)
    total_expenses = get_total_expenses(user_profile)

    # Get expenses and incomes sorted by date
    sorted_expenses = get_sorted_expenses(user_profile)
    sorted_incomes = get_sorted_incomes(user_profile)

    # Get expenses categories and amount spent in each
    expenses_categories = get_expenses_categories(user_profile)

    # Get total expenses for each month in a year
    year = datetime.now().year
    monthly_expenses = get_monthly_expenses(user_profile, year)
    monthly_income = get_monthly_income(user_profile, year)
    income_json = json.dumps(list(monthly_income), cls=CustomJSONEncoder)
    expense_json = json.dumps(list(monthly_expenses), cls=CustomJSONEncoder)

    # Get data for budget goals
    budget_goals = get_budget_goals(user_profile)

    # Get the map of expense categories with progress percentages
    budget_category_progress = get_budget_category_progress(budget_goals,user_profile)


    # Pass the gathered data to the template context
    context = {
        'transactions': transactions,
        'total_income': total_income,
        'total_expenses': total_expenses,
        'sorted_expenses': sorted_expenses,
        'sorted_incomes': sorted_incomes,
        'expenses_categories': expenses_categories,
        'monthly_expenses': expense_json,
        'monthly_income': income_json,
        'budget_goals': budget_goals,
        'username': user_profile.username,
        'budget_category_progress': budget_category_progress,
    }

    return render(request, 'tracker/pages/index_dashboard.html', context)

# Define helper functions to get the required data
def get_latest_transactions(user_profile, count):
    income_list = Income.objects.filter(user=user_profile).order_by('-datetime')[:count]
    expenses_list = Expenses.objects.filter(user=user_profile).order_by('-datetime')[:count]
    transactions = sorted(chain(income_list, expenses_list), key=lambda transaction: transaction.datetime, reverse=True)
    return transactions

def get_total_income(user_profile):
    total_income = Income.objects.filter(user=user_profile).aggregate(Sum('income_amount'))['income_amount__sum'] or 0
    return total_income

def get_total_expenses(user_profile):
    total_expenses = Expenses.objects.filter(user=user_profile).aggregate(Sum('expenses_amount'))['expenses_amount__sum'] or 0
    return total_expenses

def get_sorted_expenses(user_profile):
    sorted_expenses = Expenses.objects.filter(user=user_profile).order_by('datetime')
    return sorted_expenses

def get_sorted_incomes(user_profile):
    sorted_incomes = Income.objects.filter(user=user_profile).order_by('datetime')
    return sorted_incomes

def get_expenses_categories(user_profile):
    expenses_categories = Expenses.objects.filter(user=user_profile).values('expense_category').annotate(total_amount=Sum('expenses_amount'))
    return expenses_categories

def get_monthly_expenses(user_profile, year):
    monthly_expenses = Expenses.objects.filter(user=user_profile, datetime__year=year).values('datetime__month').annotate(total_amount=Sum('expenses_amount')).order_by('datetime__month')
    return monthly_expenses

def get_monthly_income(user_profile, year):
    monthly_income = Income.objects.filter(user=user_profile, datetime__year=year).values('datetime__month').annotate(total_amount=Sum('income_amount')).order_by('datetime__month')
    return monthly_income

def get_budget_goals(user_profile):
    budget_goals = BudgetGoal.objects.filter(user=user_profile)
    return budget_goals

from django.db.models import Sum

def get_budget_category_progress(budget_goals,user_profile):
    budget_category_progress = {}
    expenses = Expenses.objects.filter(user=user_profile)
    
    for goal in budget_goals:
        goal.total_expenses = expenses.filter(expense_category=goal.expense_category).aggregate(Sum('expenses_amount'))['expenses_amount__sum'] or 0
        goal.progress = (goal.total_expenses / goal.goal_amount) * 100 if goal.goal_amount > 0 else 0
        goal.progress = float("{:.2f}".format(goal.progress))

        budget_category_progress[goal.expense_category] = goal.progress
    
    return budget_category_progress




#pages

# views.py

from django.shortcuts import render, redirect, get_object_or_404
from .models import BudgetGoal
from .forms import BudgetGoalForm

def budget_combined(request, goal_id=None):
    user_profile = request.user
    expenses = Expenses.objects.filter(user=user_profile)
    budget_goals = BudgetGoal.objects.filter(user=user_profile)

    # If a goal_id is provided, fetch the goal to be edited
    goal_to_edit = None
    if goal_id:
        goal_to_edit = get_object_or_404(BudgetGoal, id=goal_id, user=user_profile)

    if request.method == 'POST':
        if goal_to_edit:  # If editing an existing goal
            form = BudgetGoalForm(request.POST, instance=goal_to_edit)
        else:
            form = BudgetGoalForm(request.POST)

        if form.is_valid():
            budget_goal = form.save(commit=False)
            budget_goal.user = user_profile
            budget_goal.save()
            return redirect('budget')  # Redirect back to the same page after setting/editing a goal
    else:
        if goal_to_edit:
            form = BudgetGoalForm(instance=goal_to_edit)
        else:
            form = BudgetGoalForm()

    # Calculate total expenses for tracking overall budget
    total_expenses = sum(expense.expenses_amount for expense in expenses)

    budget_category_progress = get_budget_category_progress(budget_goals,user_profile)

    return render(request, 'tracker/pages/budget.html', {'expenses': expenses, 'total_expenses': total_expenses, 'form': form, 'budget_goals': budget_goals})







from django.shortcuts import render, redirect
from .forms import ContactForm

def contact_view(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            contact_message = ContactSubmission(
                name=form.cleaned_data['name'],
                email=form.cleaned_data['email'],
                subject=form.cleaned_data['subject'],
                message=form.cleaned_data['message'],
            )
            contact_message.save()
            return redirect('dashboard')  # Redirect to a success page
    else:
        form = ContactForm()

    return render(request, 'tracker/pages/contact.html', {'form': form})





    # views.py

from django.shortcuts import render, redirect
from .models import SharedExpense
from .forms import SharedExpenseForm

def share_with_friend(request):
    user = request.user

    # Calculate the total amount shared by the user
    total_shared_amount = 0

    # Calculate the total amount others owe to the user
    total_amount_others_owe_payer = 0

    # Get all shared expenses where the user is the payer
    payer_shared_expenses = SharedExpense.objects.filter(payer=user)

    for expense in payer_shared_expenses:
        total_shared_amount += expense.amount

    # Get all shared expenses where the user is a participant
    user_shared_expenses = SharedExpense.objects.filter(participants=user)

    for expense in user_shared_expenses:
        total_participants = expense.participants.count() + 1  # Include the payer
        user_share = expense.amount / total_participants
        total_amount_others_owe_payer += user_share

    # Get a list of shared expenses
    shared_expenses = SharedExpense.objects.filter(payer=request.user)

    if request.method == 'POST':
        form = SharedExpenseForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('share_with_friend')  # Redirect back to the same page
    else:
        form = SharedExpenseForm()

    return render(request, 'tracker/pages/share_with_friends.html', {
        'total_shared_amount': total_shared_amount,
        'total_amount_others_owe_payer': total_amount_others_owe_payer,
        'shared_expenses': shared_expenses,
        'form': form,
    })


def help(request):
    return render(request, "tracker/pages/help.html")
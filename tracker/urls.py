from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path("", views.dashboard, name="home"),
    path('signup/', views.signup, name='signup'),
    path('users/', views.print_all_users, name='users'),
    path('login/', auth_views.LoginView.as_view(template_name='tracker/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),

    path('add_income/', views.add_income, name='add_income'),
    path('add_expense/', views.add_expense, name='add_expense'),
    path('edit_income/<int:income_id>/', views.edit_income, name='edit_income'),
    path('delete_income/<int:income_id>/', views.delete_income, name='delete_income'),
    path('edit_expense/<int:expense_id>/', views.edit_expense, name='edit_expense'),
    path('delete_expense/<int:expense_id>/', views.delete_expense, name='delete_expense'),
    path('income_expenses/', views.income_expenses_list, name='income_expenses_list'),
    path('transactions/', views.transaction_list, name='transactions'),

    path('budget_view/', views.budget_view, name='budget_view'),
    path('budget/', views.budget_combined, name='budget'),
    path('budget/<int:goal_id>/', views.budget_combined, name='budget_id'),
    path('edit_budget_goal/<int:goal_id>/', views.edit_budget_goal, name='edit_budget_goal'),
    path('delete_budget_goal/<int:goal_id>/', views.delete_budget_goal, name='delete_budget_goal'),

    path('financial_report/', views.financial_report, name='financial_report'),


    path('create_shared_expense/', views.create_shared_expense, name='create_shared_expense'),
    path('list_shared_expenses/', views.list_shared_expenses, name='list_shared_expenses'),
    path('debt_status/', views.debt_status, name='debt_status'),


    #  path('receipts/<int:receipt_id>/', views.receipt_detail, name='receipt_detail'),
    #  path('upload_receipts/', views.upload_receipt, name='upload_receipt'),
    #  path('receipts/', views.receipt_list, name='receipt_list'),






     path('dashboard/', views.dashboard, name='dashboard'),
     path('contact/', views.contact_view, name='contact'),
     path('share-with-friends/', views.share_with_friend, name='share_with_friend'),
     path('help/', views.help, name='help'),

    #  path('send_email/', views.send_email, name='send_email'),

]

    # path('transactions/add/', views.add_transaction, name='add_transaction'),
    # path('transactions/edit/<int:transaction_id>/', views.edit_transaction, name='edit_transaction'),
    # path('transactions/delete/<int:transaction_id>/', views.delete_transaction, name='delete_transaction'),
    # path('transactions/list/', views.transaction_list, name='transaction_list'),

    # path('transactions/createsamples',views.sampler_transaction,name='sampler_transaction'),


    # path('graphs/', views.graphs, name='graphs'),
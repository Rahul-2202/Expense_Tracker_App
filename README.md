# Expense_Tracker_App

The Expense Tracker Web App is a Django-based application designed to help users manage their finances efficiently. It provides various features to track income, expenses, savings, and budgeting. Users can also register, log in, and manage their profiles. The application aims to simplify financial management and provide insights into one's financial status.

![WhatsApp Image 2023-09-22 at 5 48 34 PM](https://github.com/Rahul-2202/Expense_Tracker_App/assets/80082925/c79aefa1-eb11-44e7-8d3f-a36abce9c58d)


<img width="929" alt="image" src="https://github.com/Rahul-2202/Expense_Tracker_App/assets/80082925/5ec3eec9-6d04-42d7-b060-1a84e9082236">

## Features

### 1. User Authentication

- Users can register and create accounts.
- Existing users can log in securely.
- User profiles can be managed, including updating personal information.

### 2. Database Structure

- The application uses Django models to structure the database.
- Supported financial data includes income sources, expense categories, and individual transactions.
- Each transaction includes a date, amount, and a description.

### 3. Transaction Management

- Users can easily add, edit, and delete income and expense transactions.
- Transactions are tracked over time to provide historical data.

### 4. Dashboard

- The user-friendly dashboard offers an overview of financial status.
- Graphical representations show income, expenses, and savings trends.
- Key financial metrics are displayed for quick reference.

### 5. Reporting

- Users can generate customized reports based on their financial data.
- Example report: Monthly income vs. expenses report.

### 6. Budgeting

- Users can set budget goals for various expense categories.
- Progress towards budget goals is tracked, helping users stay on top of their financial targets.

### 7. OAuth Integration

- Users have the option to sign up using their Google account through Django Allauth or Google's API client library.

### 8. Notification System

- A notification system is in place to inform users about budget overruns and other important financial events.
- Email notifications are sent using Sendgrid or another email service.

### 9. Expense Splitting

- Users can split expenses with others and keep track of who owes whom, simplifying shared financial responsibilities.

### 10. Receipt Uploading

- Users have the ability to upload and store receipts for their transactions, helping with record-keeping.

## Getting Started

Follow these steps to run the Expense Tracker Web App on your local server:

1. **Clone the Repository:**   
   -git clone <repository-url>

2. **Install Dependencies:**
   -pip install -r requirements.txt

3. **Apply Database Migrations:**

   -python manage.py makemigrations
   -python manage.py migrate

4. **Run the Development Server:**
   -python manage.py runserver



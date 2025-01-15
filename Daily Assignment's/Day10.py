import pandas as pd
data = pd.read_csv("C:/Users/ADMIN/Downloads/Day_10_banking_data.csv")

"""
Assignment 1: Filtering Data Based on Conditions
Tasks:
    Filter out all rows where the Transaction_Amount is greater than 2000.
    Find all rows where the Transaction_Type is "Loan Payment" and the Account_Balance is greater than 5000.
    Extract transactions made in the "Uptown" branch.
Objective:
    Practice filtering data using conditions and boolean indexing.

"""
filtered_amount = data[data['Transaction_Amount'] > 2000]
print(filtered_amount)
filtered_loan_payment = data[(data['Transaction_Type'] == 'Loan Payment') & (data['Account_Balance'] > 5000)]
print(filtered_loan_payment)
uptown_transactions = data[data['Branch'] == 'Uptown']
print(uptown_transactions)

"""
Assignment 2: Data Transformation
Tasks:
    Add a new column called Transaction_Fee, calculated as 2% of Transaction_Amount.
    Create a new column Balance_Status:
    If Account_Balance is greater than 5000, label it as "High Balance".
    Otherwise, label it as "Low Balance".
Objective:
    Learn how to create new columns and apply transformations based on existing data.

"""
data['Transaction_Fee'] = data['Transaction_Amount'] * 0.02
data['Balance_Status'] = data['Account_Balance'].apply(lambda x: 'High Balance' if x > 5000 else 'Low Balance')
print(data.head())
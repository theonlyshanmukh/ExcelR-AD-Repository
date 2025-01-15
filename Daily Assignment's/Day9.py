import pandas as pd
"""
Assignment 1: Data Exploration
Tasks:
    Load the banking_data.csv file using Pandas.
    Display the first 5 rows of the dataset.
    Use .describe() to generate basic statistics of the numerical columns (e.g., Transaction_Amount, Account_Balance).
    Check for missing values in the dataset.
Objective:
    Understand how to load and inspect the dataset.
    Use basic descriptive statistics and data integrity checks.

"""

data = pd.read_csv("C:/Users/ADMIN/Downloads/Day_9_banking_data.csv")
print(data.head())
print(data.describe())
print(data.isnull().sum())

"""
Assignment 2: Data Aggregation and Grouping
Tasks:
    Group the data by Account_Type and calculate:
        The total sum of Transaction_Amount.
        The average Account_Balance for each account type.
    Group the data by Branch and calculate:
        The total number of transactions per branch.
        The average transaction amount per branch.
Objective:
    Learn to use groupby() for aggregating data by categories.
    Gain skills in calculating grouped statistics.

"""
account_type_group = data.groupby('Account_Type')
print(account_type_group['Transaction_Amount'].sum())
print(account_type_group['Account_Balance'].mean())
branch_group = data.groupby('Branch')
print(branch_group.size())
print(branch_group['Transaction_Amount'].mean())
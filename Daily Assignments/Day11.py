"""
Assignment 1: Sorting and Ranking Data
Tasks:
    Sort the dataset by Account_Balance in descending order and display the first 10 rows.
    Create a ranking column for Transaction_Amount within each Branch:
    Use rank() to give ranks for transactions based on their amounts within each branch.
Objective:
    Learn how to sort data and apply ranking based on certain columns.

"""

import pandas as pd
data = pd.read_csv("C:/Users/ADMIN/Downloads/Day_11_banking_data.csv")
sorted_data = data.sort_values(by='Account_Balance', ascending=False)
print(sorted_data.head(10))
data['Transaction_Rank'] = data.groupby('Branch')['Transaction_Amount'].rank(ascending=False)
print(data.head())
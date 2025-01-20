"""
Assignment 1: Data Visualization
Tasks:
    Plot the total sum of Transaction_Amount per Account_Type using a bar plot.
    Create a pie chart to show the percentage of transactions per Branch.
Objective:
    Understand how to visualize data using Pandas' built-in plotting capabilities (Matplotlib integration).

"""

import pandas as pd
import matplotlib.pyplot as plt
data = pd.read_csv("C:/Users/ADMIN/Downloads/Day_12_banking_data.csv")
account_type_totals = data.groupby('Account_Type')['Transaction_Amount'].sum()
account_type_totals.plot(kind='bar', title='Total Transaction Amount per Account Type', xlabel='Account Type', ylabel='Total Transaction Amount', color='skyblue')
plt.show()
branch_counts = data['Branch'].value_counts()
branch_counts.plot(kind='pie', title='Percentage of Transactions per Branch', autopct='%1.1f%%', startangle=90)
plt.ylabel('')  
plt.show()
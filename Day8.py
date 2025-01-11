"""
Data Filtering

Extract all rows where sales are greater than 1000.
Find all sales records for a specific region (e.g., "East").

"""

import pandas as pd
data = pd.read_csv("C:/Users/ADMIN/Downloads/Day_8_sales_data.csv")
sales_above_1000 = data[data['Sales'] > 1000]
print("Rows where sales are greater than 1000:")
print(sales_above_1000)
region_sales = data[data['Region'] == 'East']
print("\nSales records for the 'East' region:")
print(region_sales)

"""
Data Processing

Add a new column, Profit_Per_Unit, calculated as Profit / Quantity.
Create another column, High_Sales, which labels rows as Yes if Sales > 1000, else No.

"""

data['Profit_Per_Unit'] = data['Profit'] / data['Quantity']
print("\nData with Profit_Per_Unit column:")
print(data.head())
data['High_Sales'] = data['Sales'].apply(lambda x: 'Yes' if x > 1000 else 'No')
print("\nData with High_Sales column:")
print(data.head())
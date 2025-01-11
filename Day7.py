"""
Load and Explore the Data

Load the sales_data.csv file using Pandas.
Display the first 5 rows of the dataset.
Print basic statistics (mean, median, min, max, etc.) of the numerical columns using .describe().

"""

import pandas as pd
data = pd.read_csv("C:/Users/ADMIN/Downloads/Day_7_sales_data.csv")
print("First 5 rows of the dataset:")
print(data.head())
print("\nBasic statistics of numerical columns:")
print(data.describe())

"""
Data Analysis

Calculate the total sales for each region.
Find the most sold product (based on quantity).
Compute the average profit margin for each product. (Profit margin = Profit / Sales * 100)

"""
total_sales_by_region = data.groupby('Region')['Sales'].sum()
print("\nTotal sales for each region:")
print(total_sales_by_region)

most_sold_product = data.groupby('Product')['Quantity'].sum().idxmax()
print("\nMost sold product (based on quantity):")
print(most_sold_product)

data['Profit Margin (%)'] = (data['Profit'] / data['Sales']) * 100
average_profit_margin = data.groupby('Product')['Profit Margin (%)'].mean()
print("\nAverage profit margin for each product:")
print(average_profit_margin)
"""
Assignment 1: Sales and Effectiveness Analysis
    Objective:
        Explore the relationship between marketing spend, sales, and drug effectiveness across different regions and age groups. Create visualizations using matplotlib and seaborn.
    Instructions:
    Load the dataset.
    Perform data cleaning (check for missing values, duplicates).
    Create the following visualizations:
        A bar plot showing total sales per region.
        A scatter plot to visualize the relationship between Marketing_Spend and Sales.
        A boxplot comparing drug effectiveness across different age groups.
        A line plot showing the sales trend for each product over different trial periods.
        A heatmap of the correlation between Sales, Marketing_Spend, and Effectiveness.
        Based on the visualizations, summarize any patterns or trends you observe.
    Expected Outcome:
        Insights on how marketing spend impacts sales.
        Analysis of which age groups have higher drug effectiveness.
        Regional sales distribution.
"""

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("C:/Users/ADMIN/Downloads/Day_13_Pharma_data.csv")

print("Column Names:", df.columns)

print("Missing Values:\n", df.isnull().sum())

df = df.dropna()
print("Duplicates:", df.duplicated().sum())
df = df.drop_duplicates()

plt.figure(figsize=(10, 6))
region_sales = df.groupby('Region')['Sales'].sum().reset_index()
sns.barplot(data=region_sales, x='Region', y='Sales', hue='Region', dodge=False, palette='viridis')
plt.title('Total Sales per Region')
plt.xlabel('Region')
plt.ylabel('Total Sales')
plt.xticks(rotation=45)
plt.legend(title='Region')
plt.show()

plt.figure(figsize=(10, 6))
sns.scatterplot(data=df, x='Marketing_Spend', y='Sales', hue='Region', palette='tab10')
plt.title('Marketing Spend vs Sales')
plt.xlabel('Marketing Spend')
plt.ylabel('Sales')
plt.legend(title='Region')
plt.show()

plt.figure(figsize=(10, 6))
sns.boxplot(data=df, x='Age_Group', y='Effectiveness', hue='Age_Group', dodge=False, palette='coolwarm')
plt.title('Drug Effectiveness Across Age Groups')
plt.xlabel('Age Group')
plt.ylabel('Effectiveness')
plt.legend(title='Age Group')
plt.show()

if 'Product_Name' in df.columns:  
    plt.figure(figsize=(12, 6))
    sns.lineplot(data=df, x='Trial_Period', y='Sales', hue='Product_Name', marker='o')
    plt.title('Sales Trend for Each Product Over Trial Periods')
    plt.xlabel('Trial Period')
    plt.ylabel('Sales')
    plt.legend(title='Product')
    plt.show()
else:
    print("Column 'Product_Name' not found. Check your dataset.")

plt.figure(figsize=(8, 6))
corr_matrix = df[['Sales', 'Marketing_Spend', 'Effectiveness']].corr()
sns.heatmap(corr_matrix, annot=True, cmap='coolwarm', fmt='.2f')
plt.title('Correlation Heatmap')
plt.show()

print("\nSummary of Insights:")
print("- Regions with the highest sales can be identified from the bar plot.")
print("- The scatter plot shows how marketing spend correlates with sales, possibly indicating diminishing returns.")
print("- Boxplots highlight which age groups experience higher drug effectiveness.")
print("- The line plot reveals sales trends over trial periods for each product, useful for tracking product performance.")
print("- The heatmap provides a quick overview of correlations between key metrics.")
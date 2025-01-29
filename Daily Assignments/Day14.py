"""
Assignment 2: Drug Effectiveness and Side Effects Comparison
    Objective:
        Compare drug effectiveness and side effects by different products, regions, and trial periods. Visualize these comparisons using matplotlib and seaborn.
    Instructions:
        Load the dataset.
        Perform any necessary data cleaning.
        Create the following visualizations:
            A bar plot comparing the average Effectiveness for each drug across different regions.
            A violin plot to show the distribution of Effectiveness and Side_Effects for each product.
            A pairplot to explore relationships between Effectiveness, Side_Effects, and Marketing_Spend.
            A boxplot comparing Effectiveness for different trial periods.
            A regression plot to analyze how Marketing_Spend affects drug Effectiveness.
        Based on the visualizations, provide an analysis of:
        Which product has the best overall effectiveness.
    The correlation between effectiveness and side effects.
    Expected Outcome:
        Insights into how the effectiveness of each drug varies by region and trial period.
        Understanding the trade-off between drug effectiveness and side effects.

"""

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("C:/Users/ADMIN/Downloads/Day_14_Pharma_data.csv")
print("Column Names:", df.columns)
print("Missing Values:\n", df.isnull().sum())
df = df.dropna()
print("Duplicates:", df.duplicated().sum())
df = df.drop_duplicates()

plt.figure(figsize=(12, 6))
avg_effectiveness = df.groupby(['Product_Name', 'Region'])['Effectiveness'].mean().reset_index()
sns.barplot(data=avg_effectiveness, x='Product_Name', y='Effectiveness', hue='Region', palette='viridis')
plt.title('Average Effectiveness of Drugs Across Regions')
plt.xlabel('Product Name')
plt.ylabel('Average Effectiveness')
plt.legend(title='Region')
plt.xticks(rotation=45)
plt.show()

plt.figure(figsize=(14, 6))
sns.violinplot(data=df, x='Product_Name', y='Effectiveness', palette='coolwarm', inner='quartile')
plt.title('Distribution of Effectiveness for Each Product')
plt.xlabel('Product Name')
plt.ylabel('Effectiveness')
plt.xticks(rotation=45)
plt.show()

plt.figure(figsize=(14, 6))
sns.violinplot(data=df, x='Product_Name', y='Side_Effects', palette='mako', inner='quartile')
plt.title('Distribution of Side Effects for Each Product')
plt.xlabel('Product Name')
plt.ylabel('Side Effects')
plt.xticks(rotation=45)
plt.show()

sns.pairplot(df[['Effectiveness', 'Side_Effects', 'Marketing_Spend']], diag_kind='kde', kind='scatter', palette='husl')
plt.suptitle('Pairplot: Effectiveness, Side Effects, and Marketing Spend', y=1.02)
plt.show()

plt.figure(figsize=(12, 6))
sns.boxplot(data=df, x='Trial_Period', y='Effectiveness', palette='muted')
plt.title('Effectiveness Across Different Trial Periods')
plt.xlabel('Trial Period')
plt.ylabel('Effectiveness')
plt.show()

plt.figure(figsize=(10, 6))
sns.regplot(data=df, x='Marketing_Spend', y='Effectiveness', scatter_kws={'alpha': 0.6}, line_kws={'color': 'red'})
plt.title('Regression Analysis: Marketing Spend vs Effectiveness')
plt.xlabel('Marketing Spend')
plt.ylabel('Effectiveness')
plt.show()

print("\nSummary of Insights:")
best_effectiveness = df.groupby('Product_Name')['Effectiveness'].mean().idxmax()
print(f"- The product with the best overall effectiveness is: {best_effectiveness}")
correlation = df['Effectiveness'].corr(df['Side_Effects'])
print(f"- The correlation between Effectiveness and Side Effects is: {correlation:.2f}")
print("- The bar plot highlights how drug effectiveness varies across regions.")
print("- Violin plots show the distribution of effectiveness and side effects for each product.")
print("- Pairplot explores relationships between effectiveness, side effects, and marketing spend.")
print("- The regression plot suggests how marketing spend impacts drug effectiveness.")

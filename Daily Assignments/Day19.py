"""
Assignment 1: Handling Missing Data in an E-Commerce Orders Dataset
    Objective:
        To analyze and clean an e-commerce dataset by identifying and handling missing values using various imputation techniques.
    Instructions:
        Load the provided dataset into Pandas.
    Identify missing data:
        Use isna() and info() functions to detect missing values.
        Compute the percentage of missing values for each column.
    Analyze missing data patterns:
        Determine whether data is MCAR, MAR, or MNAR.
        Visualize missing data patterns using seaborn.heatmap().
    Handle missing values:
        Apply different imputation techniques:
            Mean/Median imputation for numerical columns (e.g., Product_Price).
            Mode imputation for categorical columns (e.g., Product_Category).
        Forward fill or backward fill for date-related fields.
        K-Nearest Neighbors (KNN) imputation for complex cases.
    Evaluate the impact:
        Compare summary statistics before and after imputation.
        Visualize the imputed values using histograms or boxplots.
    Prepare a report:
        Document findings, methods used, and final observations.
        Submit a Jupyter Notebook with the cleaned dataset.
"""

import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.impute import KNNImputer
from sklearn.preprocessing import LabelEncoder

data = pd.read_csv("C:/Users/ADMIN/Downloads/Day 19_E-Commerce_Data.csv")

print(data.info())

missing_percent = data.isna().sum() / len(data) * 100
print(missing_percent)

plt.figure(figsize=(10, 6))
sns.heatmap(data.isna(), cmap='viridis', cbar=False, yticklabels=False)
plt.title("Missing Data Heatmap")
plt.show()

num_cols = [col for col in ['Product_Price', 'Order_Amount'] if col in data.columns]
for col in num_cols:
    data[col] = data[col].fillna(data[col].median())

cat_cols = [col for col in ['Product_Category', 'Customer_Country'] if col in data.columns]
for col in cat_cols:
    data[col] = data[col].fillna(data[col].mode()[0])

date_cols = [col for col in ['Order_Date', 'Shipping_Date'] if col in data.columns]
for col in date_cols:
    data[col] = pd.to_datetime(data[col], errors='coerce')
    data[col] = data[col].fillna(method='ffill')

if 'Order_Amount' in data.columns:
    knn_imputer = KNNImputer(n_neighbors=5)
    data[num_cols] = knn_imputer.fit_transform(data[num_cols])

label_enc = LabelEncoder()
for col in cat_cols:
    data[col] = label_enc.fit_transform(data[col])

print(data.describe())

plt.figure(figsize=(12, 5))
sns.boxplot(data=data[num_cols])
plt.title("Boxplot of Numerical Features After Imputation")
plt.show()

data.to_csv("cleaned_ecommerce_orders.csv", index=False)

print("Data Cleaning Completed Successfully!")
"""
Assignment 2: Cleaning and Preparing an E-Commerce Customer Reviews Dataset
    Objective:
        To clean and prepare a dataset containing customer reviews and ratings of e-commerce products.
    Instructions:
        Load the dataset containing customer reviews, ratings, and feedback.
    Handle missing values:
        Identify missing values in Review_Text, Rating, and Customer_Age.
        Impute missing numerical values using appropriate techniques.
        Use NLP-based techniques to handle missing textual data.
    Detect and remove duplicates:
        Use duplicated() to find repeated reviews.
        Remove or merge duplicate records.
    Handle inconsistent data:
        Standardize Rating values (ensure they range between 1-5).
        Correct spelling inconsistencies in Product_Category.
    Identify and handle outliers:
        Use boxplots to find anomalies in Product_Price and Rating.
        Apply transformation techniques if necessary.
    Prepare cleaned data for analysis:
        Convert categorical data into numerical format where required.
        Save the final cleaned dataset as a CSV file.

"""

import pandas as pd
import numpy as np
import nltk
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import LabelEncoder
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.preprocessing import StandardScaler

df = pd.read_csv("C:/Users/ADMIN/Downloads/Day 20_E-Commerce_Data.csv")

print(df.isnull().sum())

numerical_columns = ['Rating', 'Customer_Age']
imputer = SimpleImputer(strategy='median')
df[numerical_columns] = imputer.fit_transform(df[numerical_columns])

df['Review_Text'].fillna('No review provided', inplace=True)

print(f"Number of duplicate records: {df.duplicated().sum()}")
df = df.drop_duplicates()

df['Rating'] = df['Rating'].apply(lambda x: min(max(x, 1), 5))
df['Product_Category'] = df['Product_Category'].str.lower()

plt.figure(figsize=(12, 6))
plt.subplot(1, 2, 1)
sns.boxplot(x=df['Product_Price'])
plt.title('Boxplot of Product Price')
plt.subplot(1, 2, 2)
sns.boxplot(x=df['Rating'])
plt.title('Boxplot of Rating')
plt.tight_layout()
plt.show()

Q1_price = df['Product_Price'].quantile(0.25)
Q3_price = df['Product_Price'].quantile(0.75)
IQR_price = Q3_price - Q1_price
lower_bound_price = Q1_price - 1.5 * IQR_price
upper_bound_price = Q3_price + 1.5 * IQR_price

Q1_rating = df['Rating'].quantile(0.25)
Q3_rating = df['Rating'].quantile(0.75)
IQR_rating = Q3_rating - Q1_rating
lower_bound_rating = Q1_rating - 1.5 * IQR_rating
upper_bound_rating = Q3_rating + 1.5 * IQR_rating

df = df[(df['Product_Price'] >= lower_bound_price) & (df['Product_Price'] <= upper_bound_price)]
df = df[(df['Rating'] >= lower_bound_rating) & (df['Rating'] <= upper_bound_rating)]

label_encoder = LabelEncoder()
df['Product_Category'] = label_encoder.fit_transform(df['Product_Category'])

df.to_csv('cleaned_ecommerce_reviews.csv', index=False)

print(df.head())

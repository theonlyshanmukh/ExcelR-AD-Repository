"""
Assignment 1: Handling Missing Data in a Healthcare Dataset
    Objective:
        To analyze and clean a healthcare dataset by identifying and handling missing values using various imputation techniques.
    Instructions:
        Dataset Exploration:
            Load the provided healthcare dataset.
            Perform an initial exploratory data analysis (EDA) to understand the structure and missing values.
        Identify Missing Data:
            Use methods such as isna() and info() in Pandas to identify missing values.
            Calculate the percentage of missing values for each column.
        Analyze the Pattern of Missing Data:
            Determine whether data is Missing Completely at Random (MCAR), Missing at Random (MAR), or Missing Not at Random (MNAR).
            Use visualization techniques like heatmaps (seaborn.heatmap()) to analyze missing patterns.
        Impute Missing Values:
            Use different imputation techniques:
                Mean/Median/Mode imputation for numerical columns.
                Mode imputation for categorical columns.
                K-Nearest Neighbors (KNN) imputation.
                Regression imputation (if applicable).
                Compare the results of different imputation techniques.
        Evaluate the Effect of Imputation:
            Perform statistical analysis (mean, standard deviation) before and after imputation.
            Visualize the impact using boxplots or histograms.
        Report & Submission:	
            Document the steps, analysis, and insights.
            Provide a Jupyter Notebook with the implementation.

"""

import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.impute import KNNImputer
from sklearn.linear_model import LinearRegression

data = pd.read_csv("C:/Users/ADMIN/Downloads/Day_15_Healthcare_Data.csv")

print(data.info())
print(data.describe())
print(data.isna().sum())

data = pd.get_dummies(data, drop_first=True)

missing_percentage = (data.isna().sum() / len(data)) * 100
print(missing_percentage)

plt.figure(figsize=(10, 6))
sns.heatmap(data.isna(), cmap='viridis', cbar=False, yticklabels=False)
plt.title('Missing Data Heatmap')
plt.show()

num_cols = data.select_dtypes(include=['number']).columns

data_mean_imputed = data.copy()
for col in num_cols:
    data_mean_imputed[col] = data[col].fillna(data[col].mean())

data_median_imputed = data.copy()
for col in num_cols:
    data_median_imputed[col] = data[col].fillna(data[col].median())

data_mode_imputed = data.copy()
for col in data.select_dtypes(include=['object']).columns:
    data_mode_imputed[col] = data[col].fillna(data[col].mode()[0])

knn_imputer = KNNImputer(n_neighbors=5)
data_knn_imputed = data.copy()
data_knn_imputed[num_cols] = knn_imputer.fit_transform(data_knn_imputed[num_cols])

reg_data = data.copy()
for col in num_cols:
    if reg_data[col].isna().sum() > 0:
        train_data = reg_data.dropna(subset=[col])
        test_data = reg_data[reg_data[col].isna()]
        
        X_train = train_data.drop(columns=[col])
        y_train = train_data[col]
        X_test = test_data.drop(columns=[col])
        
        X_train = X_train.fillna(X_train.mean())
        X_test = X_test.fillna(X_test.mean())

        if not X_test.empty:
            model = LinearRegression()
            model.fit(X_train, y_train)
            reg_data.loc[reg_data[col].isna(), col] = model.predict(X_test)

imputed_means = pd.DataFrame({
    'Original': data.dropna()[num_cols].mean(),
    'Mean': data_mean_imputed[num_cols].mean(),
    'Median': data_median_imputed[num_cols].mean(),
    'KNN': data_knn_imputed[num_cols].mean()
})

plt.figure(figsize=(12, 6))
sns.boxplot(data=imputed_means)
plt.xticks(range(len(imputed_means.columns)), imputed_means.columns)
plt.title('Comparison of Mean Values Before and After Imputation')
plt.show()


data_mean_imputed.to_csv('healthcare_mean_imputed.csv', index=False)
data_median_imputed.to_csv('healthcare_median_imputed.csv', index=False)
data_mode_imputed.to_csv('healthcare_mode_imputed.csv', index=False)
data_knn_imputed.to_csv('healthcare_knn_imputed.csv', index=False)
reg_data.to_csv('healthcare_regression_imputed.csv', index=False)
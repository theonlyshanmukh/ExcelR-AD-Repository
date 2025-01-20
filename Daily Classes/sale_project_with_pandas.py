import pandas as pd

sales_data = {
    'TransactionID': [1, 2, 3, 4, 5],
    'CustomerID': [101, 102, 103, 104, 101],
    'Amount': [250, 300, 400, 500, 600],
    'Date': ['2025-01-01', '2025-01-02', '2025-01-03', '2025-01-04', '2025-01-05']
}

customer_data = {
    'CustomerID': [101, 102, 103, 104],
    'CustomerName': ['Alice', 'Bob', 'Charlie', 'David'],
    'Age': [30, 35, 40, 25],
    'City': ['New York', 'Los Angeles', 'Chicago', 'Houston']
}

sales_df = pd.DataFrame(sales_data)
customers_df = pd.DataFrame(customer_data)

print("Sales DataFrame:")
print(sales_df.head())

print("\nShape of sales data:", sales_df.shape)
print("\nSales data statistics:")
print(sales_df.describe())
print("Sales dataframe", sales_df)
print("customers_df", customers_df)

merged_df = pd.merge(sales_df, customers_df, on='CustomerID', how='inner')
print("\nMerged DataFrame:")
print(merged_df)

merged_df = pd.merge(sales_df, customers_df, on='CustomerID', how='inner')
print("\nMerged DataFrame:")
print(merged_df)

print("\nAccess data using `loc` (row 1):")
print(merged_df.loc[1])

print("\nAccess data using `iloc` (row 2):")
print(merged_df.iloc[2])

merged_df.loc[2, 'Age'] = None  
print(merged_df)
print("\nCheck missing values (isnull):")
print(merged_df.isnull().sum())

merged_df['Age'].fillna(merged_df['Age'].mean(), inplace=True)
print("\nData after filling missing values:")
print(merged_df)

mean_sales = merged_df.groupby('CustomerName')['Amount'].mean()
print("\nMean sales per customer:")
print(mean_sales)


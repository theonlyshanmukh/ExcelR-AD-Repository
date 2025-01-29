import pandas as pd

def read_csv_file(file_path):
    try:
        data = pd.read_csv(file_path)
        print("CSV file read successfully!")
        return data
    except Exception as e:
        print(f"Error reading the CSV file: {e}")

# Example usage
file_path = "C:/Users/ADMIN/Downloads/car_price_dataset.csv"
data = read_csv_file(file_path)
print(data.head())

feature1="Engine_Size"
feature2="Price"
correlation_value=data[feature1].corr(data[feature2])
print(f"Correlation between {feature1} and {feature2} is {correlation_value: .2f}")
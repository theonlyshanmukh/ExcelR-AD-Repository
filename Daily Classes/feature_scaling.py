import pandas as pd
from sklearn.preprocessing import MinMaxScaler

data = {
    'age': [25, 30, 35, 40, 45],
    'height': [150, 160, 170, 180, 190],
    'weight': [50, 60, 70, 80, 90]
}

df = pd.DataFrame(data)
print("Original Dataset:")
print(df)

scaler = MinMaxScaler()
normalized_data = scaler.fit_transform(df)

normalized_df = pd.DataFrame(normalized_data, columns=df.columns)  # Use 'normalized_data' instead of 'scaled_data'
print("\nNormalized Dataset (scaled to range [0,1]):")
print(normalized_df)

print("\nFeature-wise Min values After Scaling:")
print(normalized_df.min())
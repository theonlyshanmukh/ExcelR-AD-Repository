import pandas as pd
from sklearn.preprocessing import OneHotEncoder

# Sample dataset
data = {
    "customer_id": [1, 2, 3, 4],
    "gender": ["Male", "Female", "Female", "Male"],
    "city": ["Hyderabad", "pune", "Banglore", "mumbai"]
}

# Convert data to a DataFrame
df = pd.DataFrame(data)
print("Original DataFrame:")
print(df)
one_hot_encoder = OneHotEncoder(sparse_output=False)
columns_to_encode = ["gender", "city"]
encoded_data = one_hot_encoder.fit_transform(df[columns_to_encode])
encoded_columns = one_hot_encoder.get_feature_names_out(columns_to_encode)
encoded_df = pd.DataFrame(encoded_data, columns=encoded_columns)
#final_df = pd.concat([df.drop(columns=columns_to_encode), encoded_df], axis=1)
print("\nOne-hot Encoded Dataframe with sklearn:")
#print(final_df)
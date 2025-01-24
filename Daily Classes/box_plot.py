import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
np.random.seed(10)
data = pd.DataFrame({
    'value': np.concatenate([np.random.normal(0, 1, 100), np.random.normal(10, 1, 10)])
})
Q1 = data['value'].quantile(0.25)
Q3 = data['value'].quantile(0.75)
IQR = Q3 - Q1
lower_bound = Q1 - 1.5 * IQR
upper_bound = Q3 + 1.5 * IQR
outliers = data[(data['value'] < lower_bound) | (data['value'] > upper_bound)]
print(outliers)
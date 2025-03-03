import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

data = {
    'Temperature': [24, 29, 32, 35, 38, 49, 42, 45, 30, 33, 36, 37],
    'Ice_cream_sales': [200, 250, 300, 350, 400, 420, 430, 450, 270, 310, 360, 380],
    'Advertising_Budget': [50,55,60,70,75,89,85,99,60,65,70,75],  # Budget in dollars
    'Customer_count': [80, 100, 120, 140, 180, 200, 190, 210, 110, 130, 150, 170]  # Number of customers
}

df = pd.DataFrame(data)

df
sns.pairplot(df, diag_kind='kde', markers=["o"], hue='Temperature')
plt.suptitle("Pair Plot of Ice Cream Sales Data",y=1.02,fontsize=16)
plt.show()


plt.figure(figsize=(8, 6))
sns.scatterplot(data=df, x='Temperature', y='Ice_cream_sales', hue='Advertising_Budget', size='Customer_count', palette='cool', sizes=(20, 200))
plt.title('Temperature vs Ice Cream Sales')
plt.xlabel('Temperature (°C)')
plt.ylabel('Ice Cream Sales')
plt.legend(title='Advertising Budget')
plt.show()

sns.pairplot(df, diag_kind='kde', markers=["o"], hue='Temperature')
plt.show()
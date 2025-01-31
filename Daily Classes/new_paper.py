import pandas as pd
import statsmodels.formula.api as smf
file_path = "C:/Users/ADMIN/Downloads/NewspaperData.csv"
df = pd.read_csv(file_path)

df_new = df[['daily','sunday']]
df_new.info()
df_new.corr()

smf.regplot(x='daily',y='sunday',data=df)
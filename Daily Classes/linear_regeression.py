"""
Compare the prices of Ola and uber which one low price and by considering the
Below following things
Y=mx+c
Fare price is 25 for ola
No. of Km Traveled (20)
Ola: Base price is 50
Uber:base price is 35 
fare price: 50
"""
import numpy as np
from sklearn.linear_model import LinearRegression

x = np.array([20]).reshape(-1, 1)
ola_m, ola_c = 25, 50
uber_m, uber_c = 50, 35

ola_model = LinearRegression().fit(x, ola_m * x + ola_c)
uber_model = LinearRegression().fit(x, uber_m * x + uber_c)

ola_price = ola_model.predict(x)[0][0]
uber_price = uber_model.predict(x)[0][0]

print("Ola Price:", ola_price)
print("Uber Price:", uber_price)
print("Cheaper:", "Ola" if ola_price < uber_price else "Uber")
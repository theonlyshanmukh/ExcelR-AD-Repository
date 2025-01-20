"""
Using the Pandas library, perform the following tasks:

1. Create a DataFrame from the following data:
   | Name     | Age | Department   | Salary  |
   |----------|-----|--------------|---------|
   | John     | 28  | HR           | 45000   |
   | Alice    | 34  | IT           | 60000   |
   | Bob      | 23  | Marketing    | 35000   |
   | Diana    | 29  | Finance      | 50000   |
"""

import pandas as pd
data = {
    "Name": ["John", "Alice", "Bob", "Diana"],
    "Age": [28, 34, 23, 29],
    "Department": ["HR", "IT", "Marketing", "Finance"],
    "Salary": [45000, 60000, 35000, 50000]
}

df = pd.DataFrame(data)
print(df)



"""
2. Write code to:
   - Display the first 2 rows of the DataFrame.
   - Add a new column named `Bonus` where the bonus is 10% of the salary.
   - Calculate the average salary of employees in the DataFrame.
   - Filter and display employees who are older than 25.
"""


print("First 2 rows:")
print(df.head(2))

df["Bonus"] = df["Salary"] * 0.10

average_salary = df["Salary"].mean()
print("\nAverage Salary:", average_salary)

filtered_employees = df[df["Age"] > 25]
print("\nEmployees older than 25:")
print(filtered_employees)
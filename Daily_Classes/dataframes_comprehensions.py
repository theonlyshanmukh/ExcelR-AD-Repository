# DataFrame with Dictionary
import pandas as pd

# Example 1: Screen Time and Sleep Hours
screen_time = [2, 4, 6]
sleep_hours = [3, 7, 8]
stu_name = ["karthik", "vivek", "raju"]

dict1 = {
    "screen_time": screen_time,
    "sleep_hours": sleep_hours,
    "stu_name": stu_name
}
df1 = pd.DataFrame(dict1)
print("DataFrame 1:\n", df1)

# Example 2: Name, ID, and Phone Number
name = ["a", "b", "c"]
id = [1, 2, 3]
phone = [123, 124, 145]

dict2 = {
    "Name": name,
    "ID": id,
    "Phone_Number": phone
}
df2 = pd.DataFrame(dict2)
print("\nDataFrame 2:\n", df2)

# List Comprehensions
# Even numbers from a list
nums = [2, 1, 13, 15]
even_nums = [i for i in nums if i % 2 == 0]
print("\nEven Numbers:", even_nums)

# Transform words to lowercase
words = ["LOWER", "W", "PYTHON"]
lowercase = [i.lower() for i in words]
print("Lowercase Words:", lowercase)

# Identifying Palindromes in a List of Words
words = ["madam", "radar", "abc"]
palindromes = [i for i in words if i == i[::-1]]
print("Palindromes:", palindromes)

# Conditionally modify elements in a list
numbers = [-5, 3, -2, 8, -1]
non_negative = [x if x > 0 else 0 for x in numbers]
print("Non-negative Numbers:", non_negative)

# Creating a Dictionary from Two Lists
keys = ["name", "age", "city"]
values = ["bangalore", 25, "Hyderabad"]
dictionary = {k: v for k, v in zip(keys, values)}
print("Dictionary:", dictionary)

# Finding Common Elements Between Two Lists
list1 = [1, 2, 3, 4, 5]
list2 = [3, 5, 8, 9, 1]
common_elements = [i for i in list1 if i in list2]
print("Common Elements:", common_elements)

# Finding List of Squares
squares = [x ** 2 for x in range(1, 20)]
print("Squares:", squares)

# Squares of Numbers Using Dictionary Comprehension
dict_example = {"a": 12, "abc": 123, "dfe": 45}
squared_values = {key: value ** 2 for key, value in dict_example.items()}
print("Squared Values Dictionary:", squared_values)

# Student Data Analysis
students = {"abc": 85, "def": 65, "ccc": 95, "chaina": 70}
passing_students = [name for name, score in students.items() if score >= 75]
grades = {name: "A" if score >= 90 else "B" for name, score in students.items()}
print("Passing Students:", passing_students)
print("Grades:", grades)

# Organizing E-commerce Data
products = [
    {"name": "Laptop", "price": 800},
    {"name": "Smartphone", "price": 500},
    {"name": "Tablet", "price": 300}
]
affordable_products = {product["name"]: product["price"] for product in products if product["price"] <= 500}
print("Affordable Products:", affordable_products)

# Square Roots Using Tuple Comprehension
import math
numbers = [4, 6, 36]
square_roots = tuple(math.sqrt(num) for num in numbers)
print("Square Roots:", square_roots)

# Lambda Function Example
square = lambda x: x ** 2
print("Square of 5:", square(5))

# Function with Multiple Operations
def calculator(a, b, operation):
    if operation == "add":
        return a + b
    elif operation == "subtract":
        return a - b
    elif operation == "multiply":
        return a * b
    elif operation == "divide":
        return a / b
    else:
        return "Invalid operation"

print("Calculator Result:", calculator(10, 5, "add"))
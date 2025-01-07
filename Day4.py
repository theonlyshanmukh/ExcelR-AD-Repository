"""Write a Python program to calculate 
the sum of all even numbers between 1 and a given positive integer n"""

n = int(input("Enter a positive integer: "))
result = sum(i for i in range(2, n + 1, 2))
print(f"The sum of all even numbers from 1 to {n} is: {result}")
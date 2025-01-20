"""Write a Python program that takes a student's marks in three subjects as input.
If the average is greater than or equal to 90, print "Grade: A".
If the average is between 80 and 89, print "Grade: B".
If the average is between 70 and 79, print "Grade: C".
Otherwise, print "Grade: Fail".
"""

s1 = int(input("Enter marks of the first subject: "))
s2 = int(input("Enter marks of the second subject: "))
s3 = int(input("Enter marks of the third subject: "))
a = (s1 + s2 + s3) / 3
print("Grade:", "A" if a >= 90 else "B" if 80 <= a < 90 else "C" if 70 <= a < 80 else "Fail")
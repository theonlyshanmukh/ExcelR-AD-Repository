import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
import numpy as np

# Task 1: Simple Histogram Example
# Sample data: a small set of values
data = [5, 7, 7, 8, 9, 10, 10, 10, 11, 12, 11, 11]

# Create the histogram
plt.hist(data, bins=10, edgecolor='black')

# Set the title and labels for the plot
plt.title('Simple Histogram Example')
plt.xlabel('Numbers')
plt.ylabel('Count')

# Show the plot
plt.show()

##########################################################

# Task 2: Histogram using seaborn
# Corrected DataFrame with equal column lengths
datf = pd.DataFrame({
    "Season 1": [7, 7, 5, 5, 6, 3],
    "Season 2": [1, 2, 8, 4, 9, 7]  # Adjusted to have the same length as "Season 1"
})

P = sns.histplot(data=datf)
P.set(xlabel="X Label Value", ylabel="Y Label Value")
plt.show()

##########################################################

# Task 3: Histogram of Cancer Patients Age Distribution
# Simulate data: Random ages of 1000 cancer patients (assume age between 20 and 80)
np.random.seed(42)  # For reproducibility
data = np.random.randint(20, 81, 1000)  # Generate 1000 random ages between 20 and 80

# Create a histogram
plt.hist(data, bins=15, edgecolor='black', color='skyblue')

# Set the title and labels for the plot
plt.title('Histogram of Cancer Patients Age Distribution')
plt.xlabel('Age')
plt.ylabel('Number of Patients')

# Display the plot
plt.show()

##########################################################

# Task 4: Boxplot of Student Performance
# Sample data
data = {
    'semester': ['Sem 1', 'Sem 1', 'Sem 1', 'Sem 1', 'Sem 1', 'Sem 2', 'Sem 2', 'Sem 2', 'Sem 2', 'Sem 2'],
    'hours_studied': [5, 8, 10, 4, 6, 9, 11, 7, 12, 8]
}

# Create a DataFrame
df = pd.DataFrame(data)

# Create the boxplot
plt.figure(figsize=(8, 6))
sns.boxplot(x='semester', y='hours_studied', data=df)

# Set plot labels and title
plt.title('Student Performance: Hours Studied by Semester')
plt.xlabel('Semester')
plt.ylabel('Number of Hours Studied')

# Show plot
plt.show()
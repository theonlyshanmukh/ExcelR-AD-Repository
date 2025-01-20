"""
Create a Dataframe for Patient Information  and include column names as below
1)Patient Name
2) Age
3) Date of oppointment
4) Patient id
Create a dataframe name as drag_quantity that includes column names as  drag name,quantity,patient_id
Filter dataframe  to get Patient name and age <6

Merge the dataframes with inner join of Patient information and drag quantity dataframe
"""


import pandas as pd

patient_info = {
    'PatientName': ['John', 'Emma', 'Sophia', 'Michael', 'Olivia'],
    'Age': [5, 34, 2, 45, 3],
    'DateOfAppointment': ['2025-01-01', '2025-01-02', '2025-01-03', '2025-01-04', '2025-01-05'],
    'PatientID': [201, 202, 203, 204, 205]
}

drug_quantity = {
    'DrugName': ['DrugA', 'DrugB', 'DrugC', 'DrugD', 'DrugE'],
    'Quantity': [10, 20, 30, 40, 50],
    'PatientID': [201, 202, 203, 204, 205]
}

patient_df = pd.DataFrame(patient_info)
drug_quantity_df = pd.DataFrame(drug_quantity)

print("Patient DataFrame:")
print(patient_df)

print("\nDrug Quantity DataFrame:")
print(drug_quantity_df)

filtered_patient_df = patient_df[patient_df['Age'] < 6][['PatientName', 'Age']]
print("\nFiltered Patient DataFrame (Age < 6):")
print(filtered_patient_df)

merged_patient_drug_df = pd.merge(patient_df, drug_quantity_df, on='PatientID', how='inner')
print("\nMerged Patient and Drug Quantity DataFrame:")
print(merged_patient_drug_df)
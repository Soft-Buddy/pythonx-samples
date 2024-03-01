import pandas as pd

# Create a DataFrame
data = {
    'Name': ['John', 'Alice', 'Bob', 'Charlie', 'David'],
    'Age': [28, 24, 22, 30, 25],
    'Salary': [50000, 60000, 45000, 70000, 55000],
    'Department': ['HR', 'IT', 'Finance', 'IT', 'Marketing']
}

df = pd.DataFrame(data)

# Display basic information about the DataFrame
print("DataFrame Info:")
print(df.info())

# Display basic statistics of the numeric columns
print("\nSummary Statistics:")
print(df.describe())

# Sort DataFrame by 'Age' in descending order
df_sorted = df.sort_values(by='Age', ascending=False)
print("\nSorted DataFrame by Age:")
print(df_sorted)

# Filter rows where Age is greater than 25
df_filtered = df[df['Age'] > 25]
print("\nFiltered DataFrame by Age:")
print(df_filtered)

# Group by 'Department' and calculate the average salary
grouped_df = df.groupby('Department')['Salary'].mean()
print("\nAverage Salary by Department:")
print(grouped_df)

# Pivot the DataFrame
pivot_df = df.pivot_table(index='Department', columns='Name', values='Salary', aggfunc="sum", fill_value=0)
print("\nPivoted DataFrame:")
print(pivot_df)

# Apply a custom function to create a new column
df['Bonus'] = df['Salary'].apply(lambda x: x * 0.1)
print("\nDataFrame with Bonus Column:")
print(df)

# Merge DataFrame with a new set of data
data2 = {
    'Name': ['John', 'Alice', 'Bob', 'Eva', 'Frank'],
    'HiredYear': [2018, 2020, 2019, 2022, 2021],
}

df2 = pd.DataFrame(data2)

merged_df = pd.merge(df, df2, on='Name', how='left')
print("\nMerged DataFrame:")
print(merged_df)

# Save DataFrame to CSV
df.to_csv('employee_data.csv', index=False)
print("\nDataFrame saved to employee_data.csv")

import pandas as pd

# Creating a DataFrame
data = {'Name': ['Alice', 'Bob', 'Charlie'],
        'Age': [25, 30, 35],
        'City': ['New York', 'San Francisco', 'Los Angeles']}

df = pd.DataFrame(data)

# Displaying DataFrame
print("DataFrame:")
print(df)

# Basic DataFrame Information
print("\nDataFrame Info:")
print(df.info())

# Descriptive Statistics
print("\nDescriptive Statistics:")
print(df.describe())

# Selecting Columns
selected_column = df['Name']

# Selecting Rows
selected_row = df.loc[1]

# Filtering Data
filtered_data = df[df['Age'] > 30]

# Adding a New Column
df['Country'] = ['USA', 'USA', 'USA']

# Removing a Column
df.drop('Country', axis=1, inplace=True)

# Handling Missing Values
df_missing = pd.DataFrame({'A': [1, 2, np.nan], 'B': [4, np.nan, 6]})
df_missing.dropna(inplace=True)
df_missing.fillna(value=0, inplace=True)

# Grouping and Aggregating
grouped_data = df.groupby('Age').mean()

# Merging DataFrames
df1 = pd.DataFrame({'key': ['A', 'B', 'C'], 'value': [1, 2, 3]})
df2 = pd.DataFrame({'key': ['A', 'B', 'D'], 'value': [4, 5, 6]})
merged_df = pd.merge(df1, df2, on='key', how='inner')

# Reading and Writing Data
df.to_csv('output.csv', index=False)
loaded_df = pd.read_csv('output.csv')

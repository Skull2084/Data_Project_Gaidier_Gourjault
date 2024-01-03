import pandas as pd

# Load the CSV file
df = pd.read_csv('your_file.csv')

# Remove duplicate rows
df = df.drop_duplicates()

# Remove rows with any missing values
df = df.dropna()

# Example of removing rows with incoherent values (adjust as needed, age, size ...)
# example : if you have a column age and want to remove lines where age is incoherent (below 0 or above 100)
df = df[(df['age'] >= 0) & (df['age'] <= 100)]

# Save the cleaned DataFrame to a new CSV file
df.to_csv('cleaned_file.csv', index=False)


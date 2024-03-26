"""
There are several ways to delete data from a data frame. Following are some of those methods:
•   Drop Rows or Columns: Use the drop() method to remove rows or columns from the DataFrame
    based on labels or indices.
•   Filtering: Filter the DataFrame using boolean indexing to exclude rows or columns based on
    certain conditions.
•   Replace with NaN or None: Replace specific values with NaN (Not a Number) or None to
    effectively remove them from the DataFrame.
Please refer below for better understanding:
"""
import pandas as pd
import numpy as np

#   DROPPING ROWS AND COLUMNS:
"""
We can use the drop method to remove rows and columns from a dataframe. Please refer to the 
below code example.
"""
# Create a DataFrame
data = {'A': [1, 2, 3], 'B': [4, 5, 6], 'C': [7, 8, 9]}
df = pd.DataFrame(data)
print("Original dataframe:")
print(df)

# Drop rows by index
df.drop([0, 1], inplace=True)  # Drop rows with index 0 and 1
print("DataFrame after dropping rows:")
print(df)

# Drop columns by label
df.drop(columns=['B'], inplace=True)  # Drop column 'B'

print("DataFrame after dropping columns:")
print(df)
print("#"*95)
"""
Lets discuss the operations of the drop method with reference to the above code:
1.  The drop() method accepts a list of index values to remove the rows corresponding to the 
    index values. As we can see that the rows 0 and 1 were removed from the dataframe after 
    line 24 is executed.
2.  A list of column names has to be passed to the keyword argument 'columns'. The listed 
    columns are then removed from the dataframe.
3.  The keyword argument 'inplace' decides whether the drop method needs to return a new 
    dataframe object or update the existing object itself for 'False' and 'True' values 
    respectively.
"""
#   FILTERING:
"""
Filtering using boolean conditions creates a new dataframe object with rows and column 
values that satisfy the condition. Please refer to the below example:
"""
# Create a DataFrame
data = {'A': [1, 2, 3], 'B': [4, 5, 6], 'C': [7, 8, 9]}
df = pd.DataFrame(data)
print("Original Dataframe:")
print(df)

# Filter rows based on condition
df = df[df['A'] != 2]  # Exclude rows where column 'A' is equal to 2
print("DataFrame after filtering rows:")
print(df)

# Filter column values based on condition
df.loc[df['B'] % 3 != 0, 'C'] = None
print("DataFrame after filtering column values:")
print(df)
print("#"*95)

"""
In the above case we are removing we are removing rows from a dataframe and also removing 
data from a particular column in the dataframe which satisfies our condition.
"""
###############################################################################################
#   REPLACE WITH NAN OR NONE:
"""
You can replace specific values with NaN or None to effectively remove them from the DataFrame.
Please refer to the below code:
"""
# Create a DataFrame
data = {'A': [1, 2, 3], 'B': [4, 5, 6], 'C': [7, 8, 9]}
df = pd.DataFrame(data)
print("Original Dataframe:")
print(df)

# Filter column values based on condition
df.loc[df['B'] % 3 != 0, 'C'] = None
print("DataFrame after filtering column values:")
print(df)
print("#"*95)

###############################################################################################
#   DROPPING NONE OR NAN VALUES:
"""
'None' or 'NaN' values in a dataframe can be removed using the dropna() method. The dropna()
method is equipped to remove rows or columns with any or all missing values based on the 
following argument values:
• axis: Specifies the axis along which to drop missing values. Default value is 0 (rows). 
        Use axis=1 to drop columns with missing values.
• how:  Specifies the condition for dropping rows or columns.
        ►'any': Drops rows or columns with any missing values (default).
        ►'all': Drops rows or columns where all values are missing.
• thresh:   Specifies the minimum number of non-missing values required to keep the row or 
            column. If a row or column contains fewer non-missing values than the threshold, it 
            will be dropped.
• subset:   Specifies the subset of columns to consider when dropping rows. Only rows with 
            missing values in the specified columns will be dropped.

Please refer to the below code example:
"""
# Create a DataFrame with missing values
data = {
    'A': [1, np.nan, 3, np.nan],
    'B': [4, 5, np.nan, np.nan],
    'C': [7, 8, 9, 10]
}
df = pd.DataFrame(data)
print("Original DataFrame:")
print(df)

# Drop rows with any missing values
df_dropped_rows = df.dropna()
print("\nDataFrame after dropping rows with any missing values:")
print(df_dropped_rows)

# Drop columns with any missing values
df_dropped_columns = df.dropna(axis=1)
print("\nDataFrame after dropping columns with any missing values:")
print(df_dropped_columns)

# Drop rows with all missing values
df_dropped_rows_all = df.dropna(how='all')
print("\nDataFrame after dropping rows with all missing values:")
print(df_dropped_rows_all)

# Drop columns with all missing values
df_dropped_columns_all = df.dropna(axis=1, how='all')
print("\nDataFrame after dropping columns with all missing values:")
print(df_dropped_columns_all)

# Drop rows with missing values in specific columns
df_dropped_subset = df.dropna(subset=['A', 'B'])
print("\nDataFrame after dropping rows with missing values in specific columns:")
print(df_dropped_subset)

# Drop rows with missing values and specify threshold
df_dropped_threshold = df.dropna(thresh=3)
print("\nDataFrame after dropping rows with less than 3 non-missing values:")
print(df_dropped_threshold)
"""
In the previous module we covered how to add data to an existing dataframe. In this lesson
we will cover how to modify existing data in a dataframe. We can broadly classify
modification by what we intend to modify. Hence, the categories are:
►   Updating Row Index Values
►   Updating Row Values
►   Updating Column Names
►   Updating column Values
►   Updating Specific Cell Values
►   Reshape Data

Each of these categories have their sub categories. We will discover them as we go through.
Please refer below:
"""
import pandas as pd

#   UPDATING ROW INDEX VALUES:
"""
Updating row indexes involves modifying the labels or positions that identify each row in a 
DataFrame. This can include reassigning existing index labels, reindexing the DataFrame with 
new labels, or resetting the index. Following are the ways we can do that:
•   Assignment: Directly assign new index labels to the DataFrame.
•   set_index(): Set one or more columns as the new index of the DataFrame.
•   reset_index(): Reset the index of the DataFrame to the default integer index.

Below code illustrates the implementation of the ways listed above:
"""
# Create a DataFrame
df = pd.DataFrame({'A': [1, 2, 3], 'B': [4, 5, 6]}, index=['row1', 'row2', 'row3'])
print("Original DataFrame:")
print(df)

# Create a DataFrame
df = pd.DataFrame({'A': [1, 2, 3], 'B': [4, 5, 6]}, index=['row1', 'row2', 'row3'])
print("Original DataFrame:")
print(df)

# Assign new index labels
df.index = ['new_row1', 'new_row2', 'new_row3']
print("\nDataFrame after assigning new index labels:")
print(df)

# Reset index to default integer index
df.reset_index(inplace=True)
print("\nDataFrame after resetting index:")
print(df)

# Set column 'A' as the new index
df.set_index('A', inplace=True)
print("\nDataFrame after setting 'A' as the new index:")
print(df)
print("#"*95)

"""
There are a few things to note about the aspects of the above code. When we use the 
reset_index() method, the existing index values are moved into a new column. By default, 
the column containing the existing index values is named "index" unless you specify a different
name using the name parameter.
Similarly, when we use the set_index() method to set a column as the new index, the existing 
index values are removed from the index and placed into a new column. The name of the new 
column is typically the same as the previous index name unless you specify a different name 
using the drop parameter.
"""
###############################################################################################
#   UPDATING ROW VALUES:
"""
Updating row values involves modifying the data within specific rows of a DataFrame. This 
means assigning new values to existing rows. This can be done in the following ways:
•   Assignment: Assign new values to specific rows based on their index labels or positions.
•   Conditional Modification: Update row values based on specified conditions.
•   Applying Functions: Apply functions to update row values.
•   Grouping and Aggregation: Perform grouping and aggregation operations to update row values.

Please refer to the below code illustrations for the methods mentioned above. We will 
discuss more after that.
"""


def double_value(x):
    return x * 2


def square_value(x):
    return x ** 2


# Create a DataFrame
df = pd.DataFrame({'A': [1, 2, 3], 'B': [4, 5, 6]}, index=['row1', 'row2', 'row3'])
print("Original DataFrame:")
print(df)

# 1. Assignment: Assign new values to specific rows based on their index labels or positions.
df.loc['row2', 'B'] = 10
print("\nDataFrame after updating row values:")
print(df)

# 2. Conditional Modification: Update row values based on specified conditions.
df.loc[df['A'] > 1, 'B'] *= 2
print("\nDataFrame after conditionally updating row values:")
print(df)

# 3. Applying Functions: Apply functions to update row values
df['A'] = df['A'].apply(double_value)
print("\nDataFrame after applying 'apply()' method:")
print(df)

# 4. Using map() method: Apply a function to every element of the DataFrame
df_squared = df.map(square_value)
print("\nDataFrame after applying 'map()' method:")
print(df_squared)

# 5. Grouping and Aggregation: Perform grouping and aggregation operations to update row values
# Group by column 'A' and calculate the sum of column 'B'
df['B'] = df.groupby('A')['B'].transform('sum')
print("\nTransformation result:")
print(df)

# 6. Using agg() method: Apply aggregation functions to specific columns
agg_result = df.agg({'A': 'sum', 'B': 'max'})
print("\nAggregation result:")
print(agg_result)
print("#"*95)
"""
We will discuss a few of the methods we used in the above code. Please refer the following:
1.  apply(): Applies a function along an axis of the DataFrame. Useful for applying custom 
    or built-in functions to rows or columns.
2.  map(): Substitutes each value in a Series with another value. Typically used for 
    element-wise mapping of values, such as converting categorical values to numerical values.
3.  groupby(): Groups data in a DataFrame based on specified criteria. Creates a GroupBy 
    object representing grouped DataFrame groups. Allows for the application of aggregation 
    functions or transformations to each group independently.
4.  transform(): Performs group-specific computations and returns a DataFrame with the same 
    shape as the original. Applies a function to each group separately and broadcasts the 
    results back to the original DataFrame. Commonly used for group-wise normalization, 
    standardization, or other group-specific calculations.
5.  agg(): Applies aggregation functions to one or more columns of a DataFrame. Computes 
    multiple statistics for one or more columns simultaneously. Returns a Series or DataFrame 
    with the computed aggregation results.
"""
###############################################################################################
#   UPDATING COLUMN NAMES:
"""
Just like row index values we can also update the column names in a dataframe. There are a 
few ways to do it:
•   Direct Renaming: Directly rename columns using the rename() method.
•   Assignment using Columns Attribute: Assign new column names directly by updating the 
    columns attribute of the DataFrame object.

Please refer to the below code illustrations:
"""
# Create a DataFrame
df = pd.DataFrame({'A': [1, 2, 3], 'B': [4, 5, 6]}, index=['row1', 'row2', 'row3'])
print("Original DataFrame:")
print(df)

# 1. Direct Renaming: Using the rename() method
df_direct_rename = df.rename(columns={'A': 'New_A', 'B': 'New_B'})
print("\nDataFrame after updating column names using Direct Renaming:")
print(df_direct_rename)

# 2. Renaming with Mapping: Using the rename() method with a mapping dictionary
mapping = {'A': 'New_A', 'B': 'New_B'}
df_mapping_rename = df.rename(columns=mapping)
print("\nDataFrame after updating column names using Renaming with Mapping:")
print(df_mapping_rename)

# 3. Assignment using Columns Attribute
df.columns = ['New_A', 'New_B']
print("\nDataFrame after updating column names using Assignment with Columns Attribute:")
print(df)
print("#"*95)

###############################################################################################
#   UPDATING COLUMN VALUES:
"""
Updating Column Values involves modifying the values within specific columns of a DataFrame.
Here are the categories and corresponding methods for updating column values.
•   Direct Assignment: Directly assign new values to specific columns using indexing or 
    attribute assignment.
•   Conditional Modification: Update column values based on specified conditions using boolean 
    indexing or the loc[] indexer.
•   Applying Functions: Apply functions to transform column values, either element-wise or 
    row-wise, using the apply() method.
•   Grouping and Aggregation: Perform group-wise computations on column values using the 
    groupby() method followed by aggregation or transformation functions.

Please refer to the below code illustration for the above mentioned methods.
"""


def square_value(x):
    return x ** 2


# Create a DataFrame
df = pd.DataFrame({'A': [1, 2, 3], 'B': [4, 5, 6]}, index=['row1', 'row2', 'row3'])
print("Original DataFrame:")
print(df)

# 1. Direct Assignment: Assign new values to specific columns
df['A'] = [10, 20, 30]
print("\nDataFrame after updating column values using Direct Assignment:")
print(df)

# 2. Conditional Modification: Update column values based on conditions
df.loc[df['A'] > 10, 'B'] *= 2  # Double the values in column 'B' where values in column 'A' are greater than 10
print("\nDataFrame after updating column values using Conditional Modification:")
print(df)

# 3. Applying Functions: Apply functions to transform column values
df['A'] = df['A'].apply(square_value)  # Square the values in column 'A'
print("\nDataFrame after updating column values using Applying Functions:")
print(df)

# 4. Grouping and Aggregation: Perform group-wise computations on column values
# Group by column 'A' and calculate the sum of column 'B' for each group
df['B'] = df.groupby('A')['B'].transform('sum')
print("\nDataFrame after updating column values using Grouping & Aggregation:")
print(df)
print("#"*95)
###############################################################################################
#   UPDATING SPECIFIC CELL VALUES:
"""
Updating specific cells involves modifying individual values within the DataFrame. Here's a 
description of the methods for updating specific cells:
•   Direct Indexing: Directly access and modify specific cells using indexing with row and 
    column labels.
•   Using .loc[]: Use the .loc[] indexer to access and modify specific cells by row and column 
    labels.
•   Using .iloc[]: Use the .iloc[] indexer to access and modify specific cells by integer-based 
    row and column indices.
•   Using .at[]: Use the .at[] indexer to access and modify a single cell value by label.
•   Using .iat[]: Use the .iat[] indexer to access and modify a single cell value by 
    integer-based index.
Please refer to the below code illustrations.
"""
# Create a DataFrame
df = pd.DataFrame({'A': [1, 2, 3], 'B': [4, 5, 6]}, index=['row1', 'row2', 'row3'])
print("Original DataFrame:")
print(df)

# 1. Direct Indexing: Modify specific cells using indexing with row and column labels
df.at['row2', 'A'] = 20  # Modify the value in row 'row2' and column 'A'
print("\nDataFrame after updating specific cells:")
print(df)

# 2. Using .loc[]: Modify specific cells using .loc[] with row and column labels
df.loc['row3', 'B'] = 60  # Modify the value in row 'row3' and column 'B'
print("\nDataFrame after updating specific cells using .loc[]:")
print(df)

# 3. Using .iloc[]: Modify specific cells using .iloc[] with integer-based row and column indices
df.iloc[0, 1] = 40  # Modify the value in the first row and second column
print("\nDataFrame after updating specific cells using .iloc[]:")
print(df)

# 4. Using .at[]: Modify a single cell value by label
df.at['row1', 'B'] = 10  # Modify the value in row 'row1' and column 'B'
print("\nDataFrame after updating specific cells using .at[]:")
print(df)

# 5. Using .iat[]: Modify a single cell value by integer-based index
df.iat[1, 0] = 200  # Modify the value in the second row and first column
print("\nDataFrame after updating specific cells using .iat[]:")
print(df)
print("#"*95)

###############################################################################################
#   RESHAPING DATA:
"""
Reshaping in pandas involves transforming the structure of a DataFrame to better suit the 
analysis or presentation requirements. Here are the main methods for reshaping data in pandas:
•   Pivoting: Reshape the DataFrame by pivoting the values of one column into new columns. This 
    is often used to convert long-format data to wide-format data.
•   Transposing: Swap the rows and columns of a DataFrame. This is useful for changing the 
    orientation of the DataFrame.

Please refer to the below code illustrations:
"""
# Create a DataFrame for demonstration
data = {
    'Date': ['2022-01-01', '2022-01-02', '2022-01-03'],
    'Fruits': ['Apple', 'Banana', 'Orange'],
    'Quantity': [5, 15, 25]
}
df = pd.DataFrame(data)
print("Original DataFrame:")
print(df)

# 1. Pivoting: Reshape the DataFrame by pivoting one column into new columns
pivot_df = df.pivot(index='Date', columns='Fruits', values='Quantity')
print("\nDataFrame after pivoting:")
print(pivot_df)

# 2. Transposing: Swap the rows and columns of a DataFrame
transposed_df = df.transpose()
print("\nDataFrame after transposing:")
print(transposed_df)
###############################################################################################
"""
This concludes modification of dataframes.
"""











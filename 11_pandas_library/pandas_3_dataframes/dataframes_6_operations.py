"""
There are a wide range of pandas methods that operate on dataframes. We can broadly classify
them into the following categories based on the type of operation they perform. Some of
these methods and their operations have been discussed in details with examples in the
previous modules. Although all the methods falling into a category will be mentioned in this
lecture, code examples will only be provided for newly introduced methods. The categories
which we mentioned above are:
►   Creating and Loading
►   Basic Information
►   Indexing and Selection
►   Statistical Analysis
►   Data Manipulation
►   Sorting and Ranking
►   Exporting to Files
►   Visualization

We will go through each one of these categories and list the methods under these categories.
We will sometimes use data imported from the data.py module present in the same package.
Please refer below:
"""
import pandas as pd
import numpy as np
from data import pokemon_df, anime_df

#   CREATING AND LOADING:
"""
This category includes methods for creating new DataFrame objects and loading data into 
DataFrames from various sources such as CSV files, Excel files, SQL databases, JSON files, 
Parquet files and HTML tables. The methods listed under this category are as follows:
"""
# read_csv() method:
"""
Reads a CSV file into a DataFrame.
► Important Arguments:
◙       filepath_or_buffer (str or path-like or file-like): Path to the CSV file or buffer 
         containing the file.
◙       sep (str, default ','): Delimiter to use.
◙       header (int, list of int, or 'infer', default 'infer'): Row number(s) to use as the 
         column names.
◙       usecols (list-like, default None): Column names to read.
◙       dtype (dict, default None): Data types to assign to columns.
Since this method and its operations have been discussed extensively in the previous module,
we will skip code examples for this method.
"""
# read_excel() method:
"""
Reads an Excel file into a DataFrame.
► Important Arguments:
◙       io (str or path-like or ExcelFile): Path to the Excel file, file-like object, 
         or ExcelFile object.
◙       sheet_name (str, int, list, or None, default 0): Name or index of the sheet(s) to read.
◙       header (int, list of int, or 'infer', default 0): Row number(s) to use as the column 
         names.
◙       usecols (str, int, list-like, or callable, default None): Columns to read.
◙       dtype (dict, default None): Data types to assign to columns.
Since this method and its operations have been discussed extensively in the previous module,
we will skip code examples for this method.
"""
# read_json() method:
"""
Reads a JSON file into a DataFrame.
► Important Arguments:
◙       path_or_buf (str or path-like or file-like): Path to the JSON file or buffer 
         containing the file.
◙       orient (str, default 'columns'): Format of the JSON file ('records', 'split', 'table',
         etc.).
◙       dtype (bool or dict, default None): Data types to assign to columns.
Since this method and its operations have been discussed extensively in the previous module,
we will skip code examples for this method.
"""
# read_html() method:
"""
Reads HTML tables into a list of DataFrame objects.
► Important Arguments:
◙       io (str or path-like or file-like): URL or file path, or HTML content as a string.
◙       header (int or list of int, default 0): Row number(s) to use as the column names.
◙       flavor (str, default 'html5lib'): HTML parser to use ('bs4', 'lxml', 'html5lib').
Please refer to the below code example:
"""
html_file_path = "pokemon_data.html"
html_tables = pd.read_html(html_file_path)
print("\nDataFrame from Html file:")
print(html_tables[0].head())

# read_parquet() method:
"""
Reads a Parquet file into a DataFrame.
► Important Arguments:
◙       path (str or path-like): Path to the Parquet file.
◙       engine (str, default 'auto'): Parquet library to use ('pyarrow' or 'fastparquet').
◙       columns (list-like, default None): Columns to read.
◙       use_nullable_dtypes (bool, default False): Whether to use nullable data types.
Please refer to the below code example:
"""
parquet_file_path = "pokemon_data.parquet"
pokemon_df_from_parquet = pd.read_parquet(parquet_file_path)
print("\nDataFrame from Parquet file:")
print(pokemon_df_from_parquet.tail())

# read_sql() method:
"""
Reads SQL query or database table into a DataFrame.
► Important Arguments:
◙       sql (str or SQLAlchemy Selectable, default None): SQL query to execute.
◙       con (SQLAlchemy engine or DBAPI2 connection): Database connection.
◙       index_col (str, list of str, or None, default None): Column(s) to set as index.
◙       parse_dates (list-like or dict, default None): Columns to parse as dates.

"""

###############################################################################################
#   BASIC INFORMATION:
"""
These methods provide basic information about the DataFrame, such as its shape, data types of 
columns, column names, index, and a summary of descriptive statistics.The methods listed under
this category are as follows:
"""
# info() method:
"""
The info() method provides a concise summary of the DataFrame, including the data types of 
each column, the number of non-null values, and memory usage. It's useful for quickly 
understanding the structure of the DataFrame and checking for missing values. Please refer 
to the below code example:
"""
pokemon_df.info()

# head() method:
"""
The head() method returns the first n rows of the DataFrame. By default, it returns the first 
five rows. It's useful for quickly inspecting the structure and contents of the DataFrame. 
Please refer to the below code example:
"""
print(pokemon_df.head())
print(pokemon_df.head(10))

# tail() method:
"""
The tail() method returns the last n rows of the DataFrame. By default, it returns the last 
five rows. It's useful for quickly inspecting the end of the DataFrame. Please refer to the 
below code example:
"""
print(pokemon_df.tail())
print(pokemon_df.tail(10))

# describe() method:
"""
The describe() method generates descriptive statistics for numerical columns in the DataFrame,
such as count, mean, standard deviation, minimum, maximum, and quartile values. It provides 
a summary of the central tendency, dispersion, and shape of the numerical data. Please refer 
to the below code example:
"""
print(pokemon_df.describe())
print("#"*95)
###############################################################################################
#   INDEXING AND SELECTION:
"""
These methods are used for accessing and selecting data from the DataFrame based on labels or 
integer positions. The methods listed under this category are as follows:
"""
# loc[] method:
"""
The loc[] method is used to access a group of rows and columns by label(s) or a boolean array.
It allows for selection based on row and column labels. Since this method and its operations
have been discussed extensively in the previous module, we will skip code examples for this 
method.
"""
# iloc[] method:
"""
The iloc[] method is used for integer-location based indexing of rows and columns. It allows 
for selection based on integer position.Since this method and its operations
have been discussed extensively in the previous module, we will skip code examples for this 
method.
"""
# at[] method:
"""
The at[] method is used for fast label-based scalar access. It's similar to loc[] but faster 
for accessing a single value.Since this method and its operations have been discussed 
extensively in the previous module, we will skip code examples for this method.
"""
# iat[] method:
"""
The iat[] method is used for fast integer-location based scalar access. It's similar to iloc[]
but faster for accessing a single value.Since this method and its operations have been 
discussed extensively in the previous module, we will skip code examples for this method.
"""
# isin() method:
"""
The isin() method is used to filter data frames. It returns a boolean array indicating whether
each element in the DataFrame is contained in the specified values. Please refer to the 
below code example:
"""
# Create a sample DataFrame
data = {'A': [1, 2, 3, 4, 5],
        'B': ['foo', 'bar', 'baz', 'qux', 'quux']}
df = pd.DataFrame(data)

# Filter rows where column 'A' contains values 2 and 4
filtered_df = df[df['A'].isin([2, 4])]
print(filtered_df)

# where() method:
"""
The where() method is used to replace values where the condition is False. Please refer to 
the below code example:
"""
# Create a sample DataFrame
data = {'A': [1, 2, 3],
        'B': [4, 5, 6]}
df = pd.DataFrame(data)

# Apply where method to the entire DataFrame
modified_df = df.where(df > 2, 0)
print(modified_df)
"""
It is important to understand that the where() method applies on all the elements in the 
dataframe. It replaces the data that doesn't satisfy the condition. In the above case it 
checks whether the values are above 2, if not it replaces the value with 0.
"""
# query() method:
"""
The query() method is used to filter rows or select columns of a DataFrame using a boolean 
expression. Since this method and its operations have been discussed extensively in the 
previous module, we will skip code examples for this method.
"""
# filter() method:
"""
The filter() method is used to subset columns or rows of a DataFrame based on the labels
specified. Please refer to the below code example:
"""
# Create a sample DataFrame
data = {'A': [1, 2, 3],
        'B': [4, 5, 6],
        'X_A': [7, 8, 9],
        'X_B': [10, 11, 12]}
df = pd.DataFrame(data)

# Select columns with names containing 'X'
filtered_columns = df.filter(like='X')
print(filtered_columns)
print("#"*95)
"""
In the above example filter() method checks the column names creates and returns a new 
dataframe with column values whose name satisfy the filter condition.
"""
###############################################################################################
#   STATISTICAL ANALYSIS:
"""
Methods in this category are used for performing statistical analysis on DataFrame data, such 
as computing sum, mean, median, min, max, standard deviation, variance, correlation, and 
covariance. The methods listed under this category are as follows:
"""
data = {'A': [1, 2, 3],
        'B': [4, 5, 6]}
df = pd.DataFrame(data)

# sum() method:
"""
This method calculates the sum of values along the specified axis. When applied to a 
DataFrame, it returns the sum of values in each column by default. You can specify the axis 
parameter to compute row-wise sums instead. Please refer to the below code example:
"""
# Sum of values in each column
column_sums = df.sum()
print("Column Sums:")
print(column_sums)

# Sum of values in each row
row_sums = df.sum(axis=1)
print("\nRow Sums:")
print(row_sums)


# mean() method:
"""
The mean() method computes the arithmetic mean of values along the specified axis. It returns 
the average of values in each column by default. You can specify the axis parameter to 
compute row-wise means instead. Please refer to the below code example:
"""
# Mean of values in each column
column_means = df.mean()
print("Column Means:")
print(column_means)

# Mean of values in each row
row_means = df.mean(axis=1)
print("\nRow Means:")
print(row_means)


# median() method:
"""
This method calculates the median of values along the specified axis. It returns the middle 
value of sorted values in each column by default. You can specify the axis parameter to 
compute row-wise medians instead. Please refer to the below code example:
"""
# Median of values in each column
column_medians = df.median()
print("Column Medians:")
print(column_medians)

# Median of values in each row
row_medians = df.median(axis=1)
print("\nRow Medians:")
print(row_medians)


# min() method:
"""
The min() method finds the minimum value along the specified axis. It returns the smallest 
value in each column by default. You can specify the axis parameter to find row-wise minimum 
values instead. Please refer to the below code example:
"""
# Minimum value in each column
column_mins = df.min()
print("Column Minimum Values:")
print(column_mins)

# Minimum value in each row
row_mins = df.min(axis=1)
print("\nRow Minimum Values:")
print(row_mins)


# max() method:
"""
This method finds the maximum value along the specified axis. It returns the largest value 
in each column by default. You can specify the axis parameter to find row-wise maximum 
values instead. Please refer to the below code example:
"""
# Maximum value in each column
column_maxs = df.max()
print("Column Maximum Values:")
print(column_maxs)

# Maximum value in each row
row_maxs = df.max(axis=1)
print("\nRow Maximum Values:")
print(row_maxs)


# std() method:
"""
The std() method computes the standard deviation of values along the specified axis. It 
measures the dispersion of values around the mean in each column by default. You can specify 
the axis parameter to compute row-wise standard deviations instead. Please refer to the 
below code example:
"""
# Standard deviation of values in each column
column_stds = df.std()
print("Column Standard Deviations:")
print(column_stds)

# Standard deviation of values in each row
row_stds = df.std(axis=1)
print("\nRow Standard Deviations:")
print(row_stds)


# var() method:
"""
This method computes the variance of values along the specified axis. It measures the 
average of squared differences from the mean in each column by default. You can specify 
the axis parameter to compute row-wise variances instead. Please refer to the below code 
example:
"""
# Variance of values in each column
column_vars = df.var()
print("Column Variances:")
print(column_vars)

# Variance of values in each row
row_vars = df.var(axis=1)
print("\nRow Variances:")
print(row_vars)


# count() method:
"""
The count() method counts the number of non-null values along the specified axis. It returns 
the count of non-missing values in each column by default. You can specify the axis parameter 
to count row-wise non-null values instead. Please refer to the below code example:
"""
# Count of non-null values in each column
column_counts = df.count()
print("Column Non-Null Value Counts:")
print(column_counts)

# Count of non-null values in each row
row_counts = df.count(axis=1)
print("\nRow Non-Null Value Counts:")
print(row_counts)


# value_counts() method:
"""
This method computes a Series containing counts of unique values. When applied to a DataFrame,
it returns the frequency of each unique value in each column separately. Please refer to the 
below code example:
"""
column_value_counts = df['A'].value_counts()
print("Value Counts for Column 'A':")
print(column_value_counts)

# corr() method:
"""
The corr() method computes the correlation matrix of numeric columns in the DataFrame. It 
calculates the pairwise correlation coefficients between columns, indicating the strength 
and direction of linear relationships between variables. Please refer to the below code 
example:
"""
column_correlation = df.corr()
print("Column Correlation Matrix:")
print(column_correlation)

# cov() method:
"""
This method computes the covariance matrix of numeric columns in the DataFrame. It measures 
the degree to which two variables change together, indicating the direction of the linear 
relationship between variables. Please refer to the below code example:
"""
column_covariance = df.cov()
print("Column Covariance Matrix:")
print(column_covariance)
print("#"*95)

###############################################################################################
#   DATA MANIPULATION:
"""
This category includes methods for manipulating DataFrame data, such as copying DataFrames, 
dropping rows or columns, handling missing values, replacing values, updating DataFrame 
contents, merging/joining DataFrames, reshaping data using pivot and applying various 
transformations and operations to DataFrame. The methods listed under this category are as 
follows:
"""
# copy() method:
"""
The copy() method is used to create a deep copy of a DataFrame or Series. It returns a new 
object with the same data as the original, but modifications to the new object do not affect 
the original.Since this method and its operations have been discussed extensively in the 
previous module, we will skip code examples for this method.
"""
# drop() method:
"""
The drop() method is used to remove rows or columns from a DataFrame based on labels or index 
position. It returns a new DataFrame with the specified rows or columns removed. Since this 
method and its operations have been discussed extensively in the previous module, we will skip
code examples for this method.
"""
# dropna() method:
"""
The dropna() method is used to remove missing values (NaN) from a DataFrame. It returns a new 
DataFrame with rows containing missing values removed. Since this method and its operations 
have been discussed extensively in the previous module, we will skip code examples for this 
method.
"""
# fillna() method:
"""
The fillna() method is used to fill missing values in a DataFrame with specified values. It 
returns a new DataFrame with missing values replaced by the specified values. Please refer 
to the below code example:
"""
# Create a sample DataFrame with missing values
data = {'A': [1, 2, np.nan, 4, np.nan],
        'B': [5, np.nan, 7, np.nan, 9]}
df = pd.DataFrame(data)

# Fill missing values with specified value (e.g., 0)
filled_df = df.fillna(0)
print("DataFrame with missing values filled:")
print(filled_df)


# update() method:
"""
The update() method is used to modify a DataFrame by updating values in place. It updates 
values in the calling DataFrame with values from another DataFrame or Series, based on 
index. Please refer to the below code example:
"""
# Create a sample DataFrame
data = {'A': [1, 2, 3],
        'B': [4, 5, 6]}
df1 = pd.DataFrame(data)

# Create another DataFrame with new values
new_values = {'A': [10, 20]}
df2 = pd.DataFrame(new_values)

# Update df1 with values from df2
df1.update(df2)

print("Updated DataFrame:")
print(df1)
"""
The important thing to note here is that the values are updated in the columns with the same
name for common row indexes.
"""
# merge() method:
"""
The merge() method is used to combine two DataFrames based on a common column or index. It 
performs database-style joins such as inner, outer, left, and right joins. Since this method 
and its operations have been discussed extensively in the previous module, we will skip code 
examples for this method.
"""
# join() method:
"""
The join() method is used to join two DataFrames based on index (by default) or columns. It 
performs an inner or outer join between the two DataFrames. Since this method and its 
operations have been discussed extensively in the previous module, we will skip code 
examples for this method.
"""
# pivot() method:
"""
The pivot() method is used to reshape a DataFrame by pivoting the data based on column values.
It creates a new DataFrame with hierarchical index based on unique values in specified columns.
Since this method and its operations have been discussed extensively in the previous module, 
we will skip code examples for this method.
"""
# groupby() method:
"""
The groupby() method is used to group data in a DataFrame based on one or more columns. It 
returns a GroupBy object which can be used to perform operations on grouped data. Since this 
method and its operations have been discussed extensively in the previous module, 
we will skip code examples for this method.
"""
# agg() method:
"""
The agg() method is used to aggregate data in a DataFrame after grouping. It allows for 
applying multiple aggregation functions to grouped data, such as mean, sum, min, max, etc.
Since this method and its operations have been discussed extensively in the previous module, 
we will skip code examples for this method.
"""
# apply() method:
"""
The apply() method is used to apply a function along an axis of a DataFrame. It can be used to
apply custom or predefined functions to each row or column of the DataFrame. Since this 
method and its operations have been discussed extensively in the previous module, 
we will skip code examples for this method.
"""
# map() method:
"""
The map() method in the context of a DataFrame is primarily used to transform values in a 
particular column by applying a function or a dictionary. It operates on each element of the 
specified column independently and returns a new dataframe with the transformed values. 
Since this method and its operations have been discussed extensively in the previous module, 
we will skip code examples for this method.
"""
# transform() method:
"""
The transform() method is used to perform group-wise transformations on a DataFrame. It 
applies a function to each group of data and returns a DataFrame with the same shape as the
original. Since this method and its operations have been discussed extensively in the 
previous module, we will skip code examples for this method.
"""
# shift() method:
"""
The shift() method is used to shift index by desired number of periods. It returns a new 
DataFrame or Series with the index shifted by the specified number of periods. Please refer 
to the below code example:
"""
# Create a sample DataFrame
data = {'A': [10, 20, 30, 40, 50]}
df = pd.DataFrame(data)

# Shift the index by 2 periods
shifted_df = df.shift(periods=2)
print("Original DataFrame:")
print(df)
print("\nDataFrame after shifting index by 2 periods:")
print(shifted_df)


# diff() method:
"""
The diff() method is used to calculate the difference between consecutive elements in a 
DataFrame or Series. It returns a new DataFrame or Series with the differences computed. 
Please refer to the below code example:
"""
# Create a sample DataFrame
data = {'A': [1, 3, 6, 10, 15]}
df = pd.DataFrame(data)

# Calculate the difference between consecutive elements
diff_df = df.diff()
print("Difference between consecutive elements:")
print(diff_df)
print("#"*95)

###############################################################################################
#   SORTING AND RANKING:
"""
These methods are used for sorting DataFrame data either by index or by values along a 
specified axis. They also include methods for ranking data. The methods listed under this 
category are as follows:
"""
# sort_index() method:
"""
The sort_index() method sorts the DataFrame by index labels along a specified axis. It accepts
parameters such as axis, which specifies the axis along which to sort the index labels, 
ascending, which determines whether to sort in ascending or descending order, level for 
MultiIndex DataFrames, and inplace to perform the sorting operation in place if set to True.
It returns the sorted DataFrame by index labels. Please refer to the below code example
"""
# Creating a sample DataFrame
data = {'A': [3, 1, 2], 'B': [6, 5, 4]}
df = pd.DataFrame(data, index=['C', 'A', 'B'])

# Sorting DataFrame by index labels
sorted_df = df.sort_index()

print("Sorted DataFrame by index labels:")
print(sorted_df)


# sort_values() method:
"""
The sort_values() method sorts the DataFrame by values along a specified axis. It takes 
parameters like by, which specifies the column name or list of column names by which to sort 
the DataFrame, axis to specify the axis along which to sort the values, ascending to 
determine the sorting order, and inplace to perform the sorting operation in place if set 
to True. It returns the sorted DataFrame by values. Please refer to the below code example
"""
# Creating a sample DataFrame
data = {'A': [3, 1, 2], 'B': [6, 5, 4]}
df = pd.DataFrame(data)

# Sorting DataFrame by values in column 'A'
sorted_df = df.sort_values(by='A')

print("Sorted DataFrame by values in column 'A':")
print(sorted_df)


# rank() method:
"""
The rank() method computes the rank of values in the DataFrame. It considers parameters such 
as axis to specify the axis along which to rank the values, method to determine the method 
used to assign ranks to tied values (options include 'average', 'min', 'max', and 'dense'), 
and ascending to determine the order of ranking. It returns a DataFrame of ranks with the 
same shape as the original DataFrame. Please refer to the below code example
"""
# Creating a sample DataFrame
data = {'A': [3, 1, 2], 'B': [6, 5, 4]}
df = pd.DataFrame(data)

# Computing ranks of values in column 'A'
rank_df = df['A'].rank()

print("Rank of values in column 'A':")
print(rank_df)
print("#"*95)

###############################################################################################
#   EXPORTING TO FILES:
"""
These methods are used for exporting DataFrame data to various file formats, such as CSV, 
Excel, SQL databases, JSON, HTML, and Parquet. The methods listed under this category are as
follows:
"""
# to_csv() method:
"""
Saves the DataFrame to a CSV file.
► Arguments:
◙       path_or_buf (str or file handle): Path to save the CSV file.
◙       sep (str, default ','): Separator to use.
◙       header (bool or list of str, default True): Whether to write column names.
◙       index (bool, default True): Whether to write row names.
Please refer to the below code example:
"""
anime_df.to_csv('anime_data.csv', index=False)

# to_excel() method:
"""
Saves the DataFrame to an Excel file.
► Arguments:
◙       excel_writer (str, ExcelWriter, or path object): File path or ExcelWriter object.
◙       sheet_name (str, default 'Sheet1'): Name of the Excel sheet.
◙       header (bool or list of str, default True): Whether to write column names.
◙       index (bool, default True): Whether to write row names.
Please refer to the below code example:
"""
pokemon_df.to_excel('pokemon_data.xlsx', sheet_name='Pokemon', index=False)
# to_json() method:
"""
Converts the DataFrame to JSON format.
► Arguments:
◙       path_or_buf (str or file handle): Path to save the JSON file.
◙       orient (str, default 'columns'): Format of the JSON file ('records', 'split', 
        'table', etc.).
◙       date_format (str, default None): Format for date columns.
Please refer to the below code example:
"""
anime_df.to_json('anime_data.json', orient='records')

# to_html() method:
"""
Renders the DataFrame as an HTML table.
► Arguments:
◙       buf (str or file handle): File path or buffer object.
◙       columns (list-like, default None): Columns to write.
◙       index (bool, default True): Whether to write row names.
◙       escape (bool, default True): Whether to escape special characters.
Please refer to the below code example:
"""
pokemon_df.to_html('pokemon_data.html', index=False)

# to_clipboard() method:
"""
Copies the DataFrame to the system clipboard.
► Arguments:
◙       excel (bool, default None): Whether to use Excel format.
◙       sep (str, default None): Separator to use.
◙       index (bool, default None): Whether to write row names.
Please refer to the below code example:
"""
anime_df.to_clipboard(index=False)

# to_parquet() method:
"""
Writes the DataFrame to the Apache Parquet format.
► Arguments:
◙       path (str or file-like object): Path to save the Parquet file.
◙       engine (str, default 'pyarrow'): Parquet library to use ('pyarrow' or 'fastparquet').
◙       compression (str, default 'snappy'): Compression algorithm ('snappy', 'gzip', 
        'brotli', etc.).
◙       index (bool, default True): Whether to include the DataFrame index.
Please refer to the below code example:
"""
pokemon_df.to_parquet('pokemon_data.parquet', index=False)

# to_sql() method:
"""
Writes the DataFrame to a SQL database table.
► Arguments:
◙       name (str): Table name.
◙       con (SQLAlchemy engine or DBAPI2 connection): Database connection.
◙       if_exists (str, default 'fail'): What to do if the table already exists ('fail', 
        'replace', 'append').
◙       index (bool, default True): Whether to include the DataFrame index.

The code example for this section will be added when we complete database connections.
"""
print("#"*95)
###############################################################################################
#   VISUALIZATION:
"""
Visualization methods are used for creating visual representations of DataFrame data, 
including plots, histograms, box plots, and scatter plots. The methods listed under this 
category are as follows:
"""

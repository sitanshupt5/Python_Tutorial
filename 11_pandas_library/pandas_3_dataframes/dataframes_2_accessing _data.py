"""
There are different ways to access values from a dataframe. We can access values from
individual cells, columns, rows etc. We can also create a subset dataframe of an original
with the row and column values that we require. We will cover the techniques one by one. For
this module we will import data from the data.py module in the same package. The dataframe has
721 rows and the column names for the dataframe are: #,Name, Type 1, Type 2, Total,	HP,
Attack,	Defense	Sp., Atk Sp., Def, Speed, Generation, Legendary
"""
from data import pokemon_df
import pandas as pd
import numpy as np


print(pokemon_df)
print("#" * 95)
"""
The purpose of the code above this comment section is for required imports, data checks and 
for data preparation. Hence, please ignore the code above.
"""
#   1. Accessing column values in a dataframe:
"""
All the values from a particular column in a dataframe can be accessed using square 
brackets('[]') or using the dot notation. Please refer to the below code:
"""
types = pokemon_df["Type 1"]
names = pokemon_df.Name
print(types)
print()
print(names)
print()
"""
It must be noted that the dot notation can only be used if the column names do not contain 
spaces or special characters. In case of occurence of spaces and special characters only 
square brackets can be used. We can also fetch all the values in a column by using the get()
method. The get() method takes the column name as the argument and returns values for that 
column. The main difference between using get() method and square brackets is that, 
get() method does not return error in output if the column name is missing or invalid, 
rather is returns a 'None' object. The get() method also accepts a second argument for 
default which accepts a string value. The default string value is printed in case the column
name is not present in the dataframe. Please refer to the below code:
"""
print(pokemon_df.get('Names'))
print()
print(pokemon_df.get('Attacks'))    # Invalid column name
print()
print(pokemon_df.get('Attacks', 'Quick Attack'))    # Invalid column name with default value
print("#" * 95)

"""
In the above code output we can see that the get() method returns all values from the 
selected column of the dataframe. If the column name passed is invalid, it returns None or 
any other value depending on the value of the default argument.
"""

#   2. Accessing rows in a dataframe using '.loc[]' and '.iloc[]' accessors:
"""
Rows in a dataframe can be accessed using the '.loc[]' and '.iloc[]' accessors. Please refer
to the below code illustration:
"""
data_series = {'Name': pd.Series(['Alice', 'Bob', 'Charlie']), 'Age': pd.Series([25, 30, 35])}
df = pd.DataFrame(data_series)
df.index = ['row1', 'row2', 'row3']
row1 = pokemon_df.loc[0]
row2 = df.loc['row2']
print(row1)
print()
print(row2)
"""
As we can see above the loc[] accessor can access data for both integer based and label 
based row indexes and returns the value in the dataframe as a series. The index labels of 
the series are the column names of the dataframe and the corresponding values of those 
columns populate the series values respective to those columns.
The iloc[] accessor on the other hand accesses the row values based on the integer position 
of the row. The index values carry less importance. It can also access data from 
dataframes that have label based indexing. Lets see an illustration.
"""
data_series = {'Name': pd.Series(['Alice', 'Bob', 'Charlie']), 'Age': pd.Series([25, 30, 35])}
df = pd.DataFrame(data_series)
df.index = [1, 2, 3]
print(df.iloc[1])
print()
df.index = ['row2', 'row1', 'row3']
print(df.iloc[1])
print("#" * 95)
"""
Lets understand the code above. In line 56 we assign the following values to the row indexes: 
[2, 1, 3]. This means the row at index position 0 gets index value 1, the row at position 1 
gets the index value 2 and the row at position 2 gets the index value 3 for the dataframe. 
Normally when we try to access the row with index value 1 using the loc[] accessor it will 
return the first row of the dataframe. However in this case since we use the iloc operator 
we are returned the second row which has index value 2. This is because, although the second
row in the dataframe has index value 2, the index position still remains 1.
It would be more clear when we look at the second example in line 59. We have set the 
indexing of the dataframe to labels ['row2', 'row1', 'row3']. Hence, the row indexes 'row2',
'row1', 'row3' correspond to the 1st, 2nd and 3rd rows of the dataframe respectively. When 
we use the iloc[] accessor with index position 1, it refers to the second row which has 
index position 1. This also illustrates that the iloc[] accessor can access the rows of a 
dataframe using integer index positions irrespective of the index values and index types of 
the dataframe.
"""
#   3. Access cell value using the  'at[]' or 'iat[]' accessor methods.
"""
The 'at[]' and 'iat[]' accessor methods are very similar in the way the operate as compared to
'.loc[]' and '.iloc[]' accessors. The only difference is that the  'at[]' and 'iat[]' 
accessor methods take 2 arguments, index value/position and the column name. Please refer to
the below illustration.
"""
print(df.at['row1', "Name"])
print(type(df.at['row1', "Name"]))
print(pokemon_df.at[3, "Name"])
print(type(pokemon_df.at[3, "Name"]))
"""
As illustrated above the at[] accessor can use both integer based indexing and label based 
indexing to access the rows. The iat[] accessor on the other hand only accepts integer 
position for both row and column. This is irrespective of the index values of the row as the
iat[] accessor used the index position instead of the index value. Please refer below:
"""
print(df.iat[0, 1])
print(type(df.iat[0, 1]))
print(pokemon_df.iat[6, 1])
print(type(pokemon_df.iat[6, 1]))
print("#" * 95)
"""
An important thing to note when accessing the cell values of a dataframe is that the 
datatype will be the type of data contained in the column. It can be int, str, bool or any 
other python object. Please check the datatypes of the values returned above in the output.
"""
#   4. Access multiple rows and/or columns from dataframe using slicing with loc[] and iloc[]:
"""
We can slice an existing dataframe using the loc[] and iloc[] accessors. For that we have to
provide the start and end values for the row indexes and columns. Please refer below:
"""
print(df.loc['row2':'row1', 'Name':'Age'])
print()
print(pokemon_df.loc[0:10, 'Name':'Total'])
print()
print(pokemon_df.loc[:15, :'Type 1'])
print()
print(pokemon_df.loc[790:, 'Name':])
print()
print(pokemon_df.loc[0:10:2, 'Name':'Total'])
print()

"""
As we can see in the outputs of the above lines of code, we can slice our dataframe in any 
way and create a new dataframe. Similarly, we can use the iloc[] accessor method. As we 
know, iloc[] only operates on the postions of the corresponding indexes and columns rather 
than their values. Please refer to the below code:
"""
print(df.iloc[0:1, 0:1])
print()
print(pokemon_df.iloc[0:11, 1:3])
print()
print(pokemon_df.iloc[:15, :3])
print()
print(pokemon_df.iloc[790:, 1:])
print()
print(pokemon_df.iloc[1:11:2, 1:4])
print("#" * 95)

#   5. Access values from dataframe using boolean conditions:
"""
We have seen that in case of series we can access a subset of the series using boolean 
indexing. We can use the same principle on dataframes. Please refer to the below code:
"""
condition1 = pokemon_df['Type 1'] == 'Fire'
condition2 = pokemon_df['Type 2'] == 'Fire'
combined_condition = condition1 | condition2
fire_types = pokemon_df[combined_condition]
print(fire_types[fire_types['Total'] > 500])
print(fire_types[fire_types['Attack'] > 100])
"""
In the above examples we are filtering rows by applying conditions on the column data. We 
can also use boolean conditions in loc[] accessor method. Please refer to the below code:
"""
mask = pokemon_df['Total'] > 600
print(pokemon_df.loc[mask])
print("#" * 95)

#   6. Accessing index values and column names of a dataframe:
"""
We can access the index values and column names of dataframe using the '.index' and '.columns'
attributes of DataFrames class. Please refer to the code below:
"""
print(pokemon_df.index)
print(type(pokemon_df.index))
print(pokemon_df.columns)
print(type(pokemon_df.columns))
print("#" * 95)
"""
These attributes are objects of pandas RangeIndex and Index classes respectively.
"""

#   7. Accessing data from dataframe using the query() method:
"""
The query() method accepts a query condition as a string and returns output by filtering the
dataframe on the basis of the query string. Please refer to the below example: 
"""
print(pokemon_df.query('Total>600 & Legendary==True'))
print("#" * 95)
"""
The query() method returns a dataframe which is a subset of the original dataframe on which 
the query string was executed.
"""

#   8. Accessing data from a dataframe using the at_time() and between_time() methods:
"""
he at_time() and between_time() methods in Pandas are used to select rows from a DataFrame 
based on specific times when the DataFrame index is a DateTimeIndex. Please refer to the 
below example:
"""
dates = pd.date_range('2022-01-01', periods=6, freq='h')
data = {'A': np.random.randn(6), 'B': np.random.randint(0, 100, size=6)}
df = pd.DataFrame(data, index=dates)
print(df)
"""
In the above code we create a dataframe using the datetime objects as index values.
"""
print(df.at_time('02:00'))
print("#" * 95)
"""
The above code returns a single row dataframe where the date string passed as the argument 
of the at_time method is a substring of the index of the dataframe row. The at_time() method
is capable of returning dataframes with multiple rows if the index of those rows have the 
same time stamp. On the other hand between_time() method returns takes a start time and an 
end time. It returns a row/range of rows whose index in the dataframe fall between the 
start time and the end time.
"""

###############################################################################################
"""
There might definitely be other methods to access data from a dataframe. However, the above 
methods are popular.
"""


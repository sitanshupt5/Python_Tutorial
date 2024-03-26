"""
In the last lesson we covered how to access data from a dataframe in different ways. Now
that we can access data from dataframe, we can move on the modifying that data. Modifying
data in any dataframe can be done in 3 ways:
1. Adding data : In case of dataframes, adding rows, columns etc.
2. Updating data: Updating row indexes, row values, column names, column values, specific
    cells etc.
3. Deleting data: removing rows, removing columns, emptying a cell etc.

In this module we will cover adding data to an existing dataframe.
"""
import pandas as pd

#   1. Adding rows to the end of the dataframe using concat() method:
"""
We can add rows to the end of an existing dataframe using the concat() method. The new row 
to be added should be another dataframe object created from a dictionary, a list, a tuple or a 
pandas series. Please refer to the below code example:
"""
data = {
    'Column1': [1, 2, 3],
    'Column2': ['A', 'B', 'C']
}
df = pd.DataFrame(data)
column = ['Column1', 'Column2']

# New row to append
new_dict_row_df = pd.DataFrame({'Column1': 4, 'Column2': 'D'}, index=[0])
new_list_row_df = pd.DataFrame([[15, "Z"]], columns=column, index=[0])
new_tuple_row_df = pd.DataFrame([(11, "Q")], columns=column, index=[0])

# Append the new row to the DataFrame
df = pd.concat([df, new_dict_row_df], ignore_index=True)
df = pd.concat([df, new_list_row_df], ignore_index=True)
df = pd.concat([df, new_tuple_row_df], ignore_index=True)

print(df)
print("#"*95)
"""
In the above code there are a few concepts to understand. The concat() method accepts 
arguments in the form of dataframes.
In the above case in lines 28 to 30 we are creating single row dataframes where columns 
carry scalar values instead of iterables. For example refer to the dictionary:
{'Column1': 4, 'Column2': 'D'}
In this dictionary the keys Column1 and Column2 refer to int and str values (scalars) 
instead of iterables like dict, list, tuple objects etc. In such cases the keyword argument
'index=[0]' has to be specified explicitly. This is because when you provide scalar values, 
Pandas doesn't have any information to infer the shape of the DataFrame or assign an index 
automatically. Furthermore, dataframes can only be created from a list of lists, 
list of tuples, dictionaries, list of dictionaries, dictionary of lists etc. A dataframe 
cannot be created from a single list or tuple. refer to the data objects in lines 29 and 30.
Finally the ignore_index argument for concat() method in line 33 to 35. The ignore_index 
method tells the concat method to ignore the indexing on the dataframe being appended and 
create new indexes in the main dataframe.
"""

#   2. Inserting columns into and existing dataframe:
"""
We can insert new columns into the DataFrame at a specific position using the insert() method.
The insert() method takes the following arguments:
1. loc = the integer position at which the column should be inserted.
2. column = name of the new column to be inserted.
3. value = the values that need to be inserted into the new column.
Please refer to the below coded illustration:
"""
print(df)
values = ['Naruto', 'One Piece', 'Bleach', 'Demon Slayer', 'My Hero Academia', 'Haikyuu',
          'Solo Leveling']
df.insert(2, column='Column3', value=pd.Series(values))
print()
print(df)
print("#"*95)
"""
As we can see in case of the output of the above code example, we have an existing dataframe
df with two columns Column1 and Column2 and 6 rows of data. In line 67 we create a list of 
values as list. In line 69 we create and insert a new column by the name of Column3 at the 
end of the dataframe(since the dataframe had only 2 columns, value 2 passed to the loc 
argument in the insert method corresponds to the 3rd column). We name the column as Column3 
and assign values by converting our values list into a pandas Series and passing it as the 
parameter for keyword argument 'value'.
We have 7 elements in the list values, where as there are 6 rows in the dataframe. When we 
add the series as the list of values for the new column the dataframe accepts the first 6 
values in the list and ignores the last one. It is the reason we converted our list values 
into a pandas series before passing it to the 'value' argument. The value argument is 
capable to accept lists and tuples as well. However, incase of a mismatch between the number
of rows in the dataframe and the number of elements in the list or tuple, ValueError will be 
raised. Please try it.
"""
#   3. Merging dataframes using the merge() method:
"""
The merge() method in Pandas is used to merge two DataFrame objects based on the values of one 
or more keys. It offers a wide range of options for performing different types of joins, 
similar to SQL-style joins. The general syntax of the merge() method is as follows:
pd.merge(left, right, how='inner', on=None, left_on=None, right_on=None, left_index=False, 
right_index=False, suffixes=('_x', '_y'), ...)
Refer below to understand what the individual argument values mean.
•   'left', 'right' refer to the dataframes that are to be merged.
•   'how' refers to the type of join that is to be performed. The accepted values are 
    'left', 'right', 'inner', 'outer'.
•   'on' refers to the column name on which the join is to be performed.
•   'left_on' and 'right_on' Specify the column(s) to join on when the key column names are 
    different in the two DataFrames.
•   'left_index' and 'right_index' specify whether to use the indices of the DataFrames as the 
    join keys.
•   'suffixes' specify suffixes for overlapping column names in the result to avoid conflicts.

Basically the merge() method can join two dataframes in the following ways:
1.  Inner Join (how='inner'): Returns only the rows with matching keys in both DataFrames.
2.  Left Join (how='left'): Returns all rows from the left DataFrame and the matched rows from 
    the right DataFrame. Non-matching rows in the right DataFrame are filled with NaN values.
3.  Right Join (how='right'): Returns all rows from the right DataFrame and the matched rows 
    from the left DataFrame. Non-matching rows in the left DataFrame are filled with NaN values.
4.  Outer Join (how='outer'): Returns all rows from both DataFrames. Missing values are filled 
    with NaN.

Please refer to the below examples:
"""
# Create DataFrames
df1 = pd.DataFrame({'key': ['A', 'B', 'C'], 'value1': [1, 2, 3]})
df2 = pd.DataFrame({'key': ['B', 'C', 'D'], 'value2': [4, 5, 6]})

# Perform inner join
inner_join_df = pd.merge(df1, df2, on='key', how='inner')

print("Inner Join Result:")
print(inner_join_df)

# Perform left join
left_join_df = pd.merge(df1, df2, on='key', how='left')

print("Left Join Result:")
print(left_join_df)

# Perform right join
right_join_df = pd.merge(df1, df2, on='key', how='right')

print("Right Join Result:")
print(right_join_df)

# Perform outer join
outer_join_df = pd.merge(df1, df2, on='key', how='outer')

print("Outer Join Result:")
print(outer_join_df)

# Create DataFrames
df1 = pd.DataFrame({'key1': ['A', 'B', 'C'], 'key2': ['X', 'Y', 'Z'], 'value1': [1, 2, 3]})
df2 = pd.DataFrame({'key1': ['B', 'C', 'D'], 'key2': ['Y', 'Z', 'W'], 'value2': [4, 5, 6]})

# Perform merge based on multiple keys
multi_key_merge = pd.merge(df1, df2, on=['key1', 'key2'], how='inner')

print("Multi-Key Merge Result:")
print(multi_key_merge)

# Create DataFrames
df1 = pd.DataFrame({'key1': ['A', 'B', 'C'], 'value1': [1, 2, 3]})
df2 = pd.DataFrame({'key2': ['B', 'C', 'D'], 'value2': [4, 5, 6]})

# Perform merge with different key column names
merge_with_different_keys = pd.merge(df1, df2, left_on='key1', right_on='key2', how='inner')

print("Merge with Different Key Column Names Result:")
print(merge_with_different_keys)

# Create DataFrames with overlapping column names
df1_overlap = pd.DataFrame({'key': ['A', 'B', 'C'], 'value': [1, 2, 3]})
df2_overlap = pd.DataFrame({'key': ['B', 'C', 'D'], 'value': [4, 5, 6]})

# Perform merge with suffixes for overlapping column names
merge_with_suffixes = pd.merge(df1_overlap, df2_overlap, on='key', how='inner', suffixes=('_left', '_right'))

print("Merge with Suffixes for Overlapping Column Names Result:")
print(merge_with_suffixes)

# Set indices for DataFrames
df1_indexed = df1.set_index('key1')
df2_indexed = df2.set_index('key2')

# Perform merge based on indices
merge_with_indices = pd.merge(df1_indexed, df2_indexed, left_index=True, right_index=True, how='inner')

print("Merge with Indices Result:")
print(merge_with_indices)
print("#"*95)
"""
Merging DataFrames using row indexes is less common compared to merging based on column values,
but it still has its use cases depending on the data structure and analysis requirements. 
The above examples cover all the functionalities of the merge() method list of arguments.
"""

#   Joining dataframes using the join() method:
"""
The join() method in Pandas is used to join two DataFrame objects based on their index or 
column labels. It is a convenient method for combining DataFrames when the index of one 
DataFrame matches the column labels of the other DataFrame. The general syntax of the join()
method is as follows:
DataFrame.join(other, on=None, how='left', lsuffix='', rsuffix='', sort=False)
Refer below to understand what the individual argument values mean:
•   'other' refers to the other dataframe that is to be joined.
•   'on' refers to the column on which the join is to be performed.
•   'how' refers to the type of join that is to be performed. The accepted values are 
    'left', 'right', 'inner', 'outer'.
•   'lsuffix' and 'rsuffix' are the suffixes to be added to the overlapping column names of 
    the left and the right dataframes respectively.
•   'sort' value decides whether the dataframe is to be sorted on the basis of the join keys.

The join() method always performs joins on indices. Based on whether column name is passed 
to the 'on' argument the join method makes the following decisions:
◙   column name passed: The join method creates a join between the two dataframes based on 
    the values in the column(whose name is passed in the argument) of the first dataframe and 
    the index values of the second dataframe.
◙   column name not passed: In this case join method performs a join between the two 
    dataframes based on the index values of both dataframes.
Please refer to the below examples:
"""
# Create DataFrames
df1 = pd.DataFrame({'A': [1, 2, 3], 'key': ['a', 'b', 'c']})
df2 = pd.DataFrame({'B': [4, 5, 6], 'key': ['b', 'c', 'd']})

# Perform left join based on 'key' column
left_join = df1.join(df2.set_index('key'), on='key', how='left', lsuffix='_left', rsuffix='_right')

print("Column Left Join Result:")
print(left_join)

# Perform right join based on 'key' column
right_join = df1.join(df2.set_index('key'), on='key', how='right', lsuffix='_left', rsuffix='_right')

print("Column Right Join Result:")
print(right_join)

# Perform inner join based on 'key' column
inner_join = df1.join(df2.set_index('key'), on='key', how='inner', lsuffix='_left', rsuffix='_right')

print("Column Inner Join Result:")
print(inner_join)

# Perform outer join based on 'key' column
outer_join = df1.join(df2.set_index('key'), on='key', how='outer', lsuffix='_left', rsuffix='_right')

print("Column Outer Join Result:")
print(outer_join)

# Set different indices for df2
df2.index = [1, 2, 3]

# Perform left join based on indices
left_join_index = df1.join(df2, how='left', lsuffix='_left', rsuffix='_right')

print("Left Join on Indices Result:")
print(left_join_index)

# Perform right join based on indices
right_join_index = df1.join(df2, how='right', lsuffix='_left', rsuffix='_right')

print("Right Join on Indices Result:")
print(right_join_index)

# Perform inner join based on indices
inner_join_index = df1.join(df2, how='inner', lsuffix='_left', rsuffix='_right')

print("Inner Join on Indices Result:")
print(inner_join_index)

# Perform outer join based on indices
outer_join_index = df1.join(df2, how='outer', lsuffix='_left', rsuffix='_right')

print("Outer Join on Indices Result:")
print(outer_join_index)

"""
In all the above cases we have explored making joins on dataframes on columns that have the 
same names and carry potentially the same kind of data. What happens when we need to make 
joins on columns with different names in both dataframes. Unlike the merge() method the 
join() method does not provide 'left_on' and 'right_on' arguments. However, since column 
based joins between two dataframes is based on the column values of the first dataframe and 
the index values of the second dataframe, as long as we set the values of the corresponding 
column in dataframe 2 as its index values, we can perform the join. Please refer the below 
example.
"""
# Create DataFrames with different key column names
df1 = pd.DataFrame({'A': [1, 2, 3], 'key1': ['a', 'b', 'c']})
df2 = pd.DataFrame({'B': [4, 5, 6], 'key2': ['b', 'c', 'd']})

# Perform the join based on different key column names
joined_df = df1.join(df2.set_index('key2'), on='key1', how='left')

print("Joined with Different Key Column Names Result:")
print(joined_df)
print("#"*95)

#   5. Adding rows to the end of a dataframe using 'loc[]' accessor:
"""
We can add a row to the end of a dataframe using '.loc[]' accessor. Refer to the following 
code:
"""
# Create a DataFrame
df = pd.DataFrame({'A': [1, 2, 3], 'B': [4, 5, 6]}, index=[0, 1, 2])
print("Original DataFrame:")
print(df)

# Determine the new index value
new_index = df.index.max() + 1 if not df.empty else 0

# Add a new row using loc with the new index value
df.loc[new_index] = [7, 8]

print("\nDataFrame after adding a new row:")
print(df)

###############################################################################################
"""
This concludes our coverage of the ways in which we can add data to an existing dataframe.
"""
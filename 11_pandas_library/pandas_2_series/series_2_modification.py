"""
pandas Series are mutable objects. This means we can modify their elements after they have
been created. We can change the existing elements, add new elements or delete existing
elements from a series after it has been created.
However, in order to modify a specific element at a specific location, we first need to be
able to access it. Hence, first we need to learn how to access the elements.
Followed by that we will learn what are the different ways in which we can modify the
elements in a series.
"""
import pandas as pd

#   ACCESSING ELEMENTS IN A SERIES:
#   1. Using Integer Indexing:
s = pd.Series([10, 20, 30, 40, 50])
print(s[0])  # Output:   10
print(s[1:4])

"""
While using integer indexing, if we try to access the value at particular index position in 
the series, then the corresponding value is returned. We can see that in line 15 where the 
code returns the value at index position '0' in the output.
We can also use slicing to fetch a particular set of elements in the series. In such a case 
the index labels and the corresponding values are returned in the output: Please refer to 
the output of line 16 below:
1    20
2    30
3    40
dtype: int64
"""
#   2. Label Based Indexing:
"""
Let's take a look at another series this time, that has user defined string index labels.
"""
print("#" * 95)
s = pd.Series([10, 20, 30, 40, 50], index=['a', 'b', 'c', 'd', 'e'])
print(s['a'])  # Output:   10
print(s['b':'d'])

"""
In the above case we can see that we are able to access the values in the series using the 
string index labels. We can also use slicing to fetch a particular set of elements from the 
series. Please refer to the code in line 33. The output of line 33 will be the following:
b    20
c    30
d    40
dtype: int64
Just as in the case of integers, when we use slicing to fetch the values in the series, 
the values along with their corresponding index labels are returned. It is important to
note that the strings index values need not be sorted in order. The below code will make it 
more clear:
"""
s = pd.Series([10, 20, 30, 40, 50], index=['e', 'b', 'd', 'a', 'f'])
print(s['b':'f'])

"""
The output of the above lines of code will be the following:
b    20
d    30
a    40
f    50
dtype: int64

This clarifies that the index values do not have to be in order and the output values are 
returned in the order of the index values present in the series. But what is the index label
we are searching for is not present in the series at all. For example if we use code like:
print(s['b':'c'])
print(s['c'])
In such a case KeyError will be returned in output, pointing out that key 'c' is not present
in the series.
Another important thing to note is that when we compare the output values for integer slices
and string slices, is that incase of a string slice, the values at the start_index and 
end_index of the slice are both inclusive in the output. Contrary to that incase of integer 
slices the start_index value is inclusive, but the end_index value is exclusive.
It is also important to note that if a series has been created with user defined index 
labels that are strings, in such a case we cannot access directly using the integer positions.
Meaning the below code will not return us any valid output:
print(s[1])
"""
#   3. Using .loc[] and .iloc[] Accessors:
"""
'.loc[]' is primarily used label-based indexing, which means you use it to access elements 
in a Series using their index labels. Both start and stop values are included in the slices 
(just like in the case of normal label based indexing). In case of an invalid key a 
'KeyError' is raised. The Syntax for the .loc[] is as follows:
series.loc[startlabel:endlabel]
'.iloc[]' is similar to '.loc[]' except it is used for integer-bases indexing. Similar, 
to normal indexing the stop value is exclusive in case of '.iloc[]' when using slicing. It 
raises InderError if the provided integer index values are out of bounds. A key feature of 
'.iloc[]' is that we can use '.iloc[]' to access values in a series that has label based
indexing. Please refer to the below illustrations:
"""
print("#" * 95)
print(s.loc['a'])  # Single Label Indexing.
print(s.loc['b':'d'])  # Label-based slicing.

s1 = pd.Series([10, 20, 30, 40, 50])
print(s1.iloc[0])  # Single Integer Indexing.
print(s1.iloc[1:4])  # Integer-based slicing.

print(s.iloc[0])
print(s.iloc[1:4])

"""
In the code in lines 100 and 101 we are accessing values from a series with label-based 
indexing using integer values through 'iloc[]' accessor.
"""
#   4. Using Boolean Indexing:
"""
Boolean indexing in pandas Series is a powerful technique used to filter elements based on 
boolean conditions. It allows you to select elements from a Series that satisfy a specific 
condition, such as being greater than a certain value, equal to a certain value, or meeting 
any custom condition. Please refer to the below code:
"""
print(s[s > 15])
print(s[s <= 30])

"""
It is important to note that in case of Boolean indexing the condition applies on the values
rather than the index values. Boolean indexing doesn't support chained comparison. For 
example, the below line of code will raise a 'ValueError'.
print(s[10 < s < 40])
This is because python is incapable of evaluating such a value. However, such conditions can
be tested using Boolean operators
"""
print(s[(s > 10) & (s < 40)])
print(s[(s <= 10) | (s >= 40)])

#   5. Using .at[] and .iat[] Accessors:
"""
'at[]' and 'iat[]' accessors are very similar to 'loc[]' and 'iloc[]'. The only difference 
between the 2 sets is that the former is optimized for accessing single elements, where as 
the later is optimized for slicing.
"""
print("#" * 95)
print(s.at['a'])
print(s1.iat[0])
print(s.iat[0])

"""
We can also use 'iat[]' with numeric values to access values from series with label-based 
indexing. This is just like 'iloc[]'.
"""

#   6. Using the get() method:
"""
Accessing values from a series using the get() method is very similar to using the 'loc[]', 
'iloc[]', 'at[]' or 'iat[]' accessors. The only difference is that, incase of passing 
invalid index value in get() method, no error is returned. Instead a 'None' object is 
returned. The get() method also gives us the choice to return a user defined value instead 
of None incase the index is invalid. Please refer to the below code:
"""
print("#" * 95)
print(s.get('a'))                       # Output: 40
print(s1.get(0))                        # Output: 10
print(s.get('z'))                       # Output: None
print(s.get('z', 26))       # Output: 26
print(s1.get(26))                       # Output: None
print(s1.get(26, "260"))    # Output: 260

"""
As we can see from the output of the above lines of code, the get() method returns the value
from the series for a particular index. Incase, the index is not present in the series, 
then it returns 'None' object as the default value. If the default value is already passed 
in the method() call, then the default value is returned incase of the absence of index in 
the series.
"""
###############################################################################################
"""
That covers all the different ways we can use to access values from a Series instance. Now 
we can finally move to modify series. A series object can be modified in 3 ways:
1. Adding data to the Series
2. Modifying existing data in the series
3. Deleting Existing data in the series
We will take a look at all of them one by one.
"""
a = pd.Series([10, 20, 30, 40, 50, 60, 70])
b = pd.Series([10, 20, 30, 40, 50, 60, 70], index=['a', 'b', 'c', 'd', 'e', 'f', 'g'])
###############################################################################################
# ADDING DATA TO SERIES:
#   1. Using direct assignment, 'loc[]' or 'at[]':
print("#" * 95)
a[len(a)] = 80       # Using direct assignment.
a.loc[len(a)] = 90   # Using 'loc[]'
a.at[len(a)] = 100   # Using 'at[]'
print(a)

b['h'] = 80             # Using direct assignment.
b.loc['i'] = 90         # Using 'loc[]'
b.at['j'] = 100         # Using 'at[]'
print(b)

"""
It must be kept in mind that 'iloc[]' and 'iat[]' cannot be used to add data to an existing 
series. It is also important to note that in order to add new data to the series, the index 
values used should not be already present in the series. Otherwise, instead of adding data, 
existing data will be modified.
"""

#   2. Concatenating multiple series using concat() method:
print("#" * 95)
c = pd.Series([110, 120, 130], index=[10, 11, 12])
d = pd.Series({
    'k': 110,
    'l': 120,
    'm': 130
})

a = pd.concat([a, c])
print(a)

b = pd.concat([b, d])
print(b)

"""
It has to be noted that in case of concatenation the index values of both the series' being 
concatenated should be different. Although, the concatenation will go smoothly in case of 
common index values between the two series, it would cause issues accessing the values due 
to duplicate indexes. 
"""
###############################################################################################
# MODIFYING EXISTING DATA IN A SERIES:
#   1. Using direct assignment or '.loc[]' or '.at[]' accessors:
print("#" * 95)
a[10] = 200         # Using direct assignment.
a.loc[11] = 210     # Using 'loc[]'
a.at[12] = 220      # Using 'at[]'
print(a)

b['k'] = 200        # Using direct assignment.
b.loc['l'] = 210    # Using 'loc[]'
b.at['m'] = 220     # Using 'at[]'
print(b)

"""
Similar to adding new data to a series, 'iloc[]' and 'iat[]' cannot be used to modify 
existing data in a series. Also, incase of modifying existing data in a series, 
it is important that the index used already exists in the series. Otherwise data is added to
series.
"""
#   2. Using boolean indexing:
"""
We have learnt how to access data using boolean indexing. The same principle can be used to 
replace the data satisfying the new data by assigning new values. Please refer below:
"""
print("#" * 95)
a[a > 200] = 300
a[a == 100] = 200
print(a)


b[b > 200] = (b / 10) + 100
b[b == 100] = 200
print(b)

#   3. Using arithmetic operation:
"""
We can use arithmetic operations to modify the existing values in a series. In such a case 
the operation is carried out on all the elements present in the series. It is important 
to note in such a case the operations are only carried out on the values and not the 
index values. Please refer to the below code:
"""
print("#" * 95)
a = a * 2
print(a)

b = (b // 10) + 20
print(b)

"""
In the above case the operation is carried out on all the individual values in the series.
"""

#   4. Using apply() method with custom functions:
"""
The apply() method takes a custom function that carries out some kind of an operation on its
arguments and then returns the value. The operations performed can be integer, string etc.
The apply() method passes each element in the series to the custom function as an argument 
and replaces the returned value in the series. Please refer to the code below:
"""
print("#" * 95)


def operation(x):
    if x < 100:
        return x + 15
    else:
        return (x // 100) + 15


a = a.apply(operation)
print(a)

b = b.apply(operation)
print(b)

"""
Please note that when passing the function as an argument, the parenthesis surrounding the 
function should be left out. In case of the above lines of code we can check the output to 
confirm that the operations were carried out on each element of both the series'.
"""

#   5. Using the replace()  method:
"""
The replace() method is used to replace specific values existing in the series. This method 
does not require the index of the value that needs to be replaced.
"""
print("#" * 95)
a = a.replace({16: 20})
print(a)

b = b.replace({50: 10})
print(b)

"""
In the above case, the replace method takes two values, the first is the value that needs to
be searched for in the series and the second is the value that is to be replaced. If in case
the first value does not exist in the series, then the replacement does not happen. No error
error will be raised in such a case.
"""
###############################################################################################
#   DELETING EXISTING VALUES FROM A SERIES:
#   1. Using the drop() method:
print("#" * 95)
a = a.drop([2])
print(a)

b = b.drop(['f', 'h'])
print(b)

"""
The drop() method can take a single index or a range of indices (enclosed within '[]') and 
remove the values in those indices from the series. The output of the above code will show 
that the data in the concerned indices has been removed.
"""

#   2. Using '.loc[]' or '.at[]' accessors:
print("#" * 95)
a.loc[[1, 3]] = None
a.at[4] = None
print(a)

b.loc[['b', 'd']] = None
a.at['a'] = None
print(b)

"""
Removing elements from a series using the '.loc[]' or '.at[]' accessors works only on the 
values. The indexes remain intact and contain a value 'NaN'. Another important thing to note
is we can remove a range of values from a series if the series has integer based indexing.
Please refer to the code in line 313. The code will remove all the values between positions 
1 to 3 of the series and replace them with 'NaN'. On the other hand, in case of series with 
label based indexing, a similar syntax will not cover a range. Rather the values will be 
removed for the indices explicitly mentioned and be replaces with 'NaN'. Values of any 
indices in between will remain intact. Check the output for line 317. 
"""

#   3. Using boolean indexing:
"""
We can use boolean indexing to replace the values satifying the condition with None. In such
a case the values are removed however the indices remain intact and the values against those
indices are replaced with 'NaN'. Please refer to the below code:
"""
print("#" * 95)
a[a > 30] = None
print(a)

b[b > 50] = None
print(b)

#   4. Using the pop() method:
"""
Just like in the case of lists, the pop() method removes the value at the particular index 
(passed as the argument) from the series and returns the value. Please refer to the below 
code: 
"""
print("#" * 95)
a_removed_value = a.pop(7)
print(a)
print(a_removed_value)

b_removed_value = b.pop('c')
print(b)
print(b_removed_value)

"""
The pop() method removes the value entirely from the series along with its index position.
"""
#   5. Using the dropna() method:
"""
The dropna() method is used to completely remove all the 'NaN' values from the series. It 
does not require any index positions and can remove all the randomly placed 'NaN' values in 
the series in one go. Please refer to the code below:
"""
print("#" * 95)
a = a.dropna()
print(a)

b = b.dropna()
print(b)

"""
We can check in the output of the above code that all the 'NaN' values from the series' a 
and b have been removed.
"""

#   6. Using del keyword:
print("#" * 95)
del a[10]
print(a)

del b['a']
print(b)

"""
As we can see in the output of the above code, the values at the particular index positions 
have been deleted.
"""
###############################################################################################
"""
All the above code has been predominantly used to modify series containing numeric values. 
However, it is to be noted that of the above methods are going to work on string values as 
well.
"""












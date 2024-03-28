"""
There are many ways to create data frames. Data frames can be created from python data
structures or from external files such as csv, json etc. Dataframes are complex data
structures and hence, creating them requires complex combinations of python data structures.
Since, creating such data structures can be tricky and hence, we leave this job to python.
We are importing these complex data structures form the data.py module in the same package
and using them to create dataframes.
"""
import data
import pandas as pd
import numpy as np

#   1.Creating a dataframe from a list of lists:
"""
For this example we will import the pokemon_list object from the data module. pokemon_list 
is a list of lists where each contained list is synonymous to a row of data in a dataframe.
The first list in the pokemon_list list object contains the column names of the dataframe.
"""
pokemon_columns = data.pokemon_list[0]
df = pd.DataFrame(data.pokemon_list[1:], columns=pokemon_columns)
print(df)
print(type(df))
print("#"*95)
"""
In the above code we first extract the list at index 0 from the pokemon_list that contains 
the list of columns. Then we create a dataframe with the data from pokemon_list (index 1 
onwards) as the values for the dataframe and columns list extracted before as the columns data.
Note the the columns list is passed using a keyword argument. Finally we are able to create 
a dataframe df. Check the output to view the data frame.
"""

#   2.Creating a dataframe from an array of arrays (NumPy):
"""
We will read more about pythons numpy library in the numpy section. For now all we need to 
know is NumPy arrays are synonymous to python lists. Hence, an array of arrays is synonymous
to a list of lists. Please refer to the below code
"""
data_array = np.array([[1, 2, 3], [4, 5, 6]])
df = pd.DataFrame(data_array, columns=["A", "B", "C"])
print(df)
print("#"*95)

#   3.Creating a dataframe from a list of tuples:
"""
For this example we will use the anime_tuple_list as the list of tuples which we will 
convert to a dataframe. The first tuple in this list contains the column name for the data 
frame.
"""
columns = data.anime_tuple_list[0]
df = pd.DataFrame(data.anime_tuple_list[1:], columns=columns)
print(df)
print("#"*95)
"""
In the above code we extract the tuple at index 0 of the list as it contains the column 
names. We create a dataframe using rest of the tuples in the list as values of the dataframe
and use the extracted column tuple for column names.
"""
#   4.Creating a dataframe from a list of dictionaries:
"""
For this example we will use the anime_dict_list as the list of dictionaries which we will 
convert to a dataframe. In this case we will not need to provide the column name data 
separately. Since every dictionary will contain the column names as keys.
"""
df = pd.DataFrame(data.anime_dict_list)
print(df)
print("#"*95)
"""
Like mentioned above the dataframe has been created without explicitly passing the column 
names to 'columns' keyword argument.
"""

#   5.Creating a dataframe from a dictionary of lists:
"""
In a dictionary of lists, every key can correspond to a column name and the corresponding 
list values to column data. Please refer to the below code:
"""
data_dict = {'Name': ['Alice', 'Bob', 'Charlie'], 'Age': [25, 30, 35]}
df = pd.DataFrame(data_dict)
print(df)
print("#"*95)
"""
Similar to creating a dataframe from a list of dictionaries, creating a dataframe from a 
dictionary of lists does not require explicit mentioning of the column names.
"""
#   6.Creating a dataframe from a dictionary of pandas Series:
"""
We can also create a dataframe from a dictionary of pandas series. Please like the above 
cases with the involvement of dictionaries in the data structure we do not need to 
explicitly pass the columns name in the arguments. Please refer to the code below:
"""
data_series = {'Name': pd.Series(['Alice', 'Bob', 'Charlie']), 'Age': pd.Series([25, 30, 35])}
df = pd.DataFrame(data_series)
print(df)
print("#"*95)

#   7.Creating a dataframe from a csv file:
"""
We can create a dataframe from a csv file using the read_csv() method. Please refer to the 
below code.
"""
df = pd.read_csv("pokemon.csv")
print(df)
"""
We can also create a dataframe from selective columns of a csv file like illustrated in the 
code below:
"""
df = pd.read_csv("pokemon.csv", usecols=["Name", "Type 1"])
print(df)
print("#"*95)

#   8.Creating a dataframe from a json file:
"""
We can create a dataframe from a an existing json file. Please refer to the following code:
"""
df = pd.read_json("tv-shows.json")
print(df)
print("#"*95)

"""
In this case the keys in the individual json-objects are used as column names. Hence, 
there is no need for passing the column names in argument explicitly.
"""

#   9.Creating a dataframe from an excel file(.xlsx):
"""
We can create a dataframe from an existing excel file i.e with a file with 'xlsx' 
extension. Please refer to the below code:
"""
df = pd.read_excel("my_animelist.xlsx")
print(df)
print("#"*95)

#   10. Creating a dataframe with label indexes:
"""
Till we have created dataframes where the rows are integer indexed. Each index there 
corresponds to a row in the dataframe. Just like pandas series it entirely possible to index a
dataframe with labels. This can be be done by adding index list to the dataframe after it is
created. This is just like we did in case of pandas Series objects. Please refer to the below
code:
"""
data_series = {'Name': pd.Series(['Alice', 'Bob', 'Charlie']), 'Age': pd.Series([25, 30, 35])}
df = pd.DataFrame(data_series)
df.index = ['row1', 'row2', 'row3']
print(df)
print("#"*95)

"""
It is to be kept in mind that the index list should contain the exact number of elements as 
the rows in the dataframe. Incase of mismatch between the number of index values and the 
number of rows in the dataframe ValueError will be raised for length mismatch.
"""
###############################################################################################
"""
Dataframes can also be created by executing queries on database tables, html files or from 
urls that return data in the form of csv or html. These will be covered later when we cover 
database operations.
"""

"""
Although we covered most of the operational functionalities of pandas Series in the previous
module, but those were only specific to methods exclusively applicable to Series. Also,
we were using python data structures as our sources for data for the Series. What about
external sources. What about converting other objects to series? All of those will be
covered in this excercise.
In the following excercise we will import a csv file using the available pandas utilities
and operate on the data to finally convert it into a pandas Series form. For this we will
need the following methods:
1.  read_csv(): This pandas method reads data from a csv file and converts it into a DataFrame.
    It accepts many different types of parameters. The majorly important one being the 'file
    name/path' parameter and the 'usecols' parameter. The file name parameter is
    self-explanatory. The 'usecols' parameter accepts a list of columns to import.
2.  squeeze(): The squeeze() method converts a pandas DataFrame to a pandas Series.

The entire argument list of the pandas read_csv() method can be referred to from the
following link: https://pandas.pydata.org/docs/reference/api/pandas.read_csv.html

For this example we are using the pokemon.csv file which we will import to our code through
the read_csv() method.
"""
import pandas as pd

pokemon_dataframe1 = pd.read_csv("pokemon.csv")
print(pokemon_dataframe1)
print(type(pokemon_dataframe1))

"""
In the output of the above code we can see that the contents of the entire csv file has been
imported and stored an object referred by the variable pokemon_dataframe1. When we check 
the type of the object that 'pokemon_dataframe1'is in line 26, we get the output: 
"<class 'pandas.core.frame.DataFrame'>".
A DataFrame is another pandas data structure which unlike a series is 2 dimensional. The 
closest analogy would be: if series is a set of rows in a single column, then dataframe is 
a set of multiple rows and columns.
In the above code we are importing data from all the columns in the csv file in the 
dataframe. However, it is possible to import data only from selected columns from the csv 
file to the data frame. For that we have to use the 'usecols' argument. The 'usecols' 
argument as mentioned above accepts a list columns and returns the values for those columns.
"""
pokemon_dataframe2 = pd.read_csv("pokemon.csv", usecols=["Name", "Type 1"])
print("#"*95)
print(pokemon_dataframe2)

"""
As we can see in the output of the above code we get a dataframe containing data from 2 rows
of the csv file. We will discuss more about Dataframes later.
We can create a pandas series from a dataframe using the squeeze method now. 
Please refer to the below code:
"""
df = pd.read_csv("pokemon.csv", usecols=["Name"])
print("#"*95)
pokemon_series1 = df.squeeze("columns")
print(pokemon_series1)
print(type(pokemon_series1))

"""
We can see that the dataframe object created in line 51 is converted to a series in line 53 
using the squeeze() method. It is important to note that only a dataframe with one column 
can be converted to a pandas series using the squeeze() method. If there are more than one 
columns then the squeeze() method will still return a dataframe object.
There is a way to convert a dataframe with multiple columns to a pandas series. Please refer
to the code below:
"""
print("#"*95)
df = pd.read_csv("pokemon.csv")
pokemon_series2 = df.set_index("Name")["Type 1"].squeeze()
print(pokemon_series2)
print(type(pokemon_series2))

"""
In the above case we are setting the index values of the dataframe using the values from one
of the columns. Then we are selecting the values from one particular column through 
indexing( with column name) to extract a dataframe with one single column from an existing 
dataframe. Then we use the squeeze method to convert the single column dataframe extracted 
into a pandas Series.
Before we conclude this excercise we might as well take a look at the head() and the tail() 
methods for pandas Series.
1.  head(): This method returns the first n rows ('n' passed as argument value to the method)
    from the top of the series. It returns first 5 rows by default if no parameters passed 
    to the method.
2.  tail(): This method returns the last n rows ('n' passed as argument value to the method)
    of the series. It returns the last 5 rows by default if parameter is passed to the method.
Lets apply these methods to the series created above.
"""
print("#"*95)
first = pokemon_series2.head()
print(first)
print("#"*95)
first10 = pokemon_series2.head(10)
print(first10)
print("#"*95)
last = pokemon_series2.tail()
print(last)
print("#"*95)
last10 = pokemon_series2.tail(10)
print(last10)

"""
As we can see above the head() and the tail() methods return a pandas Series which is a 
subset of the original series they are operating on.
"""


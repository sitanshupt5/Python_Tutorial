"""
The pandas Series is a one-dimensional labeled array. A series combines the best features of a
list and dictionary. Series maintains a single collection of ordered values (i.e a single
column of data). We can assign each value an identifier which does not have to be unique.
In this module we will cover the different ways to create pandas series.
We can create a pandas series in the following ways:
1.  From lists
2.  From tuples
3.  From NumPy arrays
4.  From dictionaries
5.  With labeled indexes
We will take a look at all of the above one by one.
"""
import pandas as pd
import numpy as np

animes = ["Naruto", "One Piece", "DragonBall", "Bleach", "My Hero Academia", "Demon Slayer"]
big3 = ("naruto", "one piece", "bleach")
chars = ["Naruto", "Luffy", "Ichigo"]
main_chars = {
    "naruto": "Naruto",
    "one piece": "Luffy",
    "bleach": "Ichigo"
}

"""
In the above code we have created list, tuple and dictionary data that we will be using to 
create a pandas Series. In order to create a pandas series we have to create a Series class 
object by initialising the constructor with the data structure passed as an argument.
"""
#   CREATING A SERIES FROM A LIST:
anime = pd.Series(animes)
print(anime)
print(type(anime))
print("#"*95)

#   CREATING A SERIES FROM A TUPLE:
popular_animes = pd.Series(big3)
print(popular_animes)
print(type(popular_animes))
print("#"*95)

#   CREATING A SERIES FROM A NUMPY ARRAY:
chars_arr = np.array(chars)
chars_series = pd.Series(chars_arr)
print(chars_series)
print(type(chars_series))
print("#"*95)

"""
In the case of the above code blocks we see that the Series objects returned are always 
following the same template. We will take the output of the first code block between lines 
32 adn 34 as a sample:
0              Naruto
1           One Piece
2          DragonBall
3              Bleach
4    My Hero Academia
5        Demon Slayer
dtype: object
<class 'pandas.core.series.Series'>

In the above output we see that although we passed a list to create a Series, which only 
represents a row or column of data, the output we get has two columns of data. Each value in
our list is labeled with index numbers starting from 0.
In a series object, data is always labelled. It is possible for us to provide the index 
values that would be used for labelling. However, in the absence of the index values, 
numbers are used starting from 0 to index.
We can also observe that the order of the elements in the list is still maintained in the 
series.
We also see a line "dtype: object". It is the last line when we print an series object. This
signifies that the data within the list are objects. It might be confusing as we know the 
the contents of the list are actually strings. However strings are also objects of the str 
class in python. Unless, it is a primary data type (integer, float, boolean) it returns the 
value of dtype as 'object'.
Finally, the type of the series object is returned as "<class 'pandas.core.series.Series'>".
"""

#   CREATING A SERIES FROM A DICTIONARY:
mcs = pd.Series(main_chars)
print(mcs)
print(type(mcs))
print("#"*95)

"""
In case of the above code block, we have a dictionary which contains key and value pairs. 
Hence, when we convert a dictionary into a series, it takes the dictionary keys are the 
index labels. We do not have to explicitly mention the index labels in this case. Following 
is the output of the code between lines 80 and 82:
naruto       Naruto
one piece     Luffy
bleach       Ichigo
dtype: object
<class 'pandas.core.series.Series'>
"""
# CREATING SERIES WITH LABELLED INDICES USING LISTS AND TUPLES:
series_mcs = pd.Series(chars, index=big3)
print(series_mcs)
print(type(series_mcs))

"""
The output of the code between lines 97 to 99 is as follows:
naruto       Naruto
one piece     Luffy
bleach       Ichigo
dtype: object
<class 'pandas.core.series.Series'>

This shows we can use two sequence data types with same number of elements to create a 
series of data and its index labels. We can see from the above code that it is relatively 
simple to create a pandas Series object. In the next module we will take a look at the 
different ways we can access and modify the elements in a series.
"""






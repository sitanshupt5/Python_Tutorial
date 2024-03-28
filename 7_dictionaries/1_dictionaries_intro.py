"""
Dictionaries are another type of data structure used in python just like lists and tuples.
However, unlike lists and tuples, dictionaries are non sequence data types. Hence,
the values/ items stored in a dictionary cannot be accessed using index positions.
Instead, dictionaries are mutable unordered collections of key-value pairs. The keys are
used to access the individual values from a dictionaries. A Python 'dict' is an equivalent
of JAVA HashMap.
Dictionaries are defined using curly braces {}, and each key-value pair is separated by a
colon. Please refer below for more details on dictionaries.
"""
# CREATING A DICTIONARY:-
"""
There are many ways of creating. Please refer below for some of the popular ways that  are 
used.
"""
#   1. Using Curly Braces:
vehicles = {
    "dream": "Honda 250T",  # Each set of key value pairs is separated from the other by a ','.
    'roadster': 'BMW R1100',
    'er5': 'Kawasaki ER5',
    'cam-am': 'Bombardier Can-Am 250',
    'virago': 'Yamaha XV250',
    'tenere': 'Yamaha XT650',
    'jimny': 'Suzuki Jimny 1.5',
    'fiesta': 'Ford Fiesta Ghia 1.4'
}

#   2. Using 'dict' function:
team = dict(t1='Sitanshu', t2='Shivam', t3='Rajyalaxmi', t4='Puneet')
"""
In this case since the assignment operator is used instead of ':', the rules change a bit:
i. key names are treated as variables. Hence, not surrounded by '.
ii. since key names are treated as variable they cannot start with a numerical.
"""

# ACCESSING DATA FROM A DICTIONARY:-
"""
There are a few different ways to access the data from a dictionary. Please refer below for 
some of the popular ways that are used.
"""
#   1. Using the index:
my_car = vehicles['fiesta']
print(my_car)

#   2. Using the get() method:
teammate = team.get("t3")
print(teammate)

"""
Both of the above 2 methods have their pros and cons. While using both of them one has too 
keep in mind that it is imperative provide the exact key name.
1.  If we are trying to access values from a dictionary using index value and the keyname 
    provided for the index does not match with any keyname in the dictionary, then program will 
    crash.
2.  However, if we are using the get() method to access value from the dictionary and we 
    provide invalid keyname, the value returned by the get() method is None. The program 
    doesn't fail. This can be both useful and problematic. get() method also allows to 
    provide a second argument for default value in the key is not present. In this case the 
    value returned will be the default value passed in the argument.
3.  Accessing values through indices is quicker than using the get() method.
"""

#   ITERATING OVER A DICTIONARY:
"""
There are many ways to iterate over a dictionary in python. Some of them are:
1.  Iterating through keys using .keys() method.
2.  Iterating through values using .values() method.
3.  Iterating through both keys and values using .items() method.
Please refer to the illustrations below.
"""
#   Iterating through keys using .keys() method:
print("#"*95)
for key in vehicles.keys():
    print(f"{key}: {vehicles.get(key)}")

#   Iterating through values using .values() method:
print("#"*95)
for value in vehicles.values():
    print(f"{value}, ")

#   Iterating through keys and values using .items() method:
print("#"*95)
for key, value in vehicles.items():
    print(f"{key}: {value} ")

"""
It is also possible to iterate over a dictionary through keys without using the .keys() method.
This is because when we use for loop to iterate over a dictionary the default behavior is to 
iterate over the keys of the dictionary. Hence, we can skip using the .keys() method and it 
should still work just fine.
"""
#   Iterating through keys without using the .keys() method:
print("#"*95)
for key in vehicles:
    print(f"{key}: {vehicles.get(key)}")


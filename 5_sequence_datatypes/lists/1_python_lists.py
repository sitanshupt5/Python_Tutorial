"""
Lists are built-in datatype in python that allows to store a collection of items in an
ordered manner. i.e.items can be retrieved in the same order that they are stored. Lists
are mutable data types, meaning lists can be modified after creation or initiation.
Lists in python can be created by enclosing elements within '[]' separated by ','.
We can also create empty lists to which data can be added later on. The elements in a list
can belong to the same or different datatypes.
"""
# Example 1: declaring, initiating and iterating over a list.
computer_parts = ["cpu",
                  "monitor",
                  "keyboard",
                  "mouse",
                  "printer",
                  "sound box"]

for part in computer_parts:
    print(part)

# Example 2: Fetching index values and slicing a list
print(computer_parts[2])  # Fetching the value in the second index.
print(computer_parts[-1])  # Fetching the value in the last index.
print(computer_parts[0:3])  # Fetching a slice of the list between the corresponding indices.

"""
Indexing and slicing work mostly the same for strings and lists since both are sequence 
data types. However, the major difference between string and lists is that strings are
immutable where as lists are mutable. Meaning the contents of a list can be changed where
as the contents of a string cannot be changed once assigned.
"""
"""
Python sequence datatypes have a few operations that are common for both mutable and 
immutable objects. These are:- in, not in, concatenation (using +), *, fetching items
using indexes, slicing the sequence(with or without steps), len(), min(), max(), 
index() and count().
There are a few operations unique to mutable sequences in python, these are:-
del, slice, append(), clear(), copy(), insert(), pop(), remove(), reverse()
"""
# Common sequence operations
even = [2, 4, 6, 8]
odd = [1, 3, 5, 7, 9]

print(min(even))
print(max(even))
print(min(odd))
print(max(odd))
print(len(even))
print(len(odd))
print("mississippi".count("i"))         # number of occurrences of i.
print("mississippi".index("i", 5, 11))  # index of 1st occurrence of i between 5th and 11th index
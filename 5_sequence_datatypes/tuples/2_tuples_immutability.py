"""
Tuples are immutable. Hence once a tuple has been declared and initialized it is not
allowed to modify the size or contents of the tuple. Doing so would result in error.
Please refer to the following examples:
"""
book1 = ("Count of Monte Cristo", "Alexander Dumas", 1844)
print(book1)
print(book1[0])
print(book1[1])
print(book1[2])
"""
The above code will return the following output:
('Count of Monte Cristo', 'Alexander Dumas', 1844)
Count of Monte Cristo
Alexander Dumas
1844

Now say we try to change the contents and replace the author name with some other name.
"""
book1[1] = "Charles Dickens"

# Line 20 will return error: TypeError: 'tuple' object does not support item assignment.
"""
Following are few of the reasons why tuples are preferred over lists in certain circumstances:
1. Tuples protect the integrity of the data. Once the tuple has been created its contents
can never be changed.
2. Since tuples dont have overhead method required to change them, they consume less 
memory than lists.
3. Unlike lists unpacking a tuple is risk free. Since tuples are immutable, the size of 
a tuple does not change during runtime. Hence, unpacking a tuple would never lead to a 
program crashing. 
"""
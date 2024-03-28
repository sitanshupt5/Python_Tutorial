# UNPACKING INTRODUCTION:
"""
Unpacking in Python refers to the process of extracting values from iterable objects (like
tuples, lists, or strings) and assigning them to individual variables in a single line of
code. It allows you to assign multiple values at once, making the code more concise and
readable.
Unpacking is a common operation for tuples, although its uses are not limited to tuples
only. Please refer to the following example:
"""
tuple1 = ("Sitanshu", "Shivam", "Karthik")
a, b, c = tuple1
print(a)
print(b)
print(c)
"""
In the above example the values "Sitanshu", "Shivam" and "Karthik" get assigned to 3
different variable a, b and c respectively in a single line of code in line 10.
Unpacking can be used in case of lists and string as well. However, the immutable aspect
of tuples make them ideal for unpacking.
Please refer to the following unpacking examples for lists and strings.
"""
# For Lists:
list1 = [1, 2, 3]
x, y, z = list1
print(x)
print(y)
print(z)
# For Strings:
str1 = "and"
i, j, k = str1
print(i)
print(j)
print(k)

"""
It is important to note that the number of variable on the left side of the assignment
matches the number of elements in the iterable on the right side. Otherwise, 'ValueError'
will be returned.
"""

# UNPACKING PRACTICAL USES:
"""
Tuples can be used instead of individual variables wherever enumerate() function is used 
in loops. Please refer the below example:
"""
for t in enumerate("sitanshu"):
    index, character = t
    print(index, character)
"""
In the above code 't' is the temporary tuple variable.
Unpacking also tends to make the code more readable incase of tuples. Please refer the
following:
"""
book1 = ("Count of Monte Cristo", "Alexander Dumas", 1844)
book2 = ("Gullivers Travels", "Jonathon Swift", 1726)
book3 = ("David Copperfield", "Charles Dickens", 1850)
book4 = ("Old Man and the Sea", "Earnest Hemingway", 1951)
book5 = ("Time Machine", "H.G Wells", 1895)

# Printing the contents of book1 can be done by printing the values using indices:
print(book1[0])
print(book1[1])
print(book1[2])

# It can also be done through unpacking:
book_name, author, year_of_publish = book1
print(book_name)
print(author)
print(year_of_publish)
print()

"""
Comparing both the code in the 2nd method looks more readable. We can use unpacking more
effectively using loops and enumerate() function.
"""
books = (book1, book2, book3, book4, book5)

for index, book in enumerate(books, start=1):
    print("Book Index:", index)
    title, author, year = book
    print("Title:", title)
    print("Author:", author)
    print("Year:", year)
    print()
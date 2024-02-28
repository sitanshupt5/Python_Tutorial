"""
In Python, the join() method is a string method that concatenates the elements of an
iterable (e.g., list, tuple) into a single string, using a specified delimiter.
Here's the general syntax of the join() method:
delimiter.join(iterable)
Please refer the below examples:
"""
hokages = [
    "Hashirama",
    "Tobirama",
    "Hiruzen",
    "Minato",
    "Tsunade",
    "Kakashi",
    "Naruto"
]

for hokage in hokages:
    print(hokage+", ")
"""
In line 19 syntax will print all the characters in separate lines. However, there will be a ","
after the character in the last iteration. Instead of that we can manage the entire iteration
in one line of code while properly separating the items.
"""
print(", ".join(hokages))
"""
It is important to remember that join method is used to iterate through iterables like
lists and tuples. Also, these iterables must be homogenous and contain only strings.
"""
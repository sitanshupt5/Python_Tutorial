"""
A nested tuple in Python is a tuple that contains one or more tuples as its elements.
Each inner tuple can be accessed using indexing. The elements of the inner tuples can also
be accessed using nested indexing.
Nested tuples can be created with any level of nesting, depending on the requirements.
Just like regular tuples, nested tuples are immutable, meaning their elements cannot be
modified once the tuple is created.
There are many different ways to create nested tuples in python. Here are a few of them:
1. Direct Initialization
2. Tuple Concatenation
There are other methods to create tuples like 'comprehensions' and 'loops'. However, they
will be covered later. Please refer below for the examples of Direct Initialization and
Tuple Concatenation.
"""
# DIRECT INITIALIZATION:
nested_tuple1 = ((1, 2, 3), ('a', 'b', 'c'), (True, False))
print(nested_tuple1)

# TUPLE CONCATENATION:
tuple1 = (1, 2, 3)
tuple2 = ('a', 'b', 'c')
tuple3 = (True, False)
nested_tuple2 = (tuple1, tuple2, tuple3)
print(nested_tuple2)
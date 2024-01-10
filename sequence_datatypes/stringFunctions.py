"""
It is possible to concatenate strings with numerics. In java this was done automatically
by the compiler. However, in python although it doesn't happen automatically, still it can
be achieved. Following are few of the methods:
"""
# Using str() function to convert datatype to string.
age = 31
print("My age is "+str(age)+" years")
"""
However, in this method we are converting the non string value to string before the 
concatenation and in case of large code this could be tedious to repeat ever single time.
Hence, there is a much easier way to achieve this using the format function.
"""
print("My age is {0} years".format(age))
"""
The format() function takes different values as arguments and sequentially replaces them
in the appropriate indices marked in the string.These marked indices are refered to as
replacement fields.format function accepts multiple data types.
Also, multiple arguments can be passed to the format function which are sequentially stored
in the indices. The said values in the indices can be called multiple times in the string
using the replacement field number. Please refer the below example.
"""
print("""Jan:{2}, Feb:{0}, Mar:{2}, Apr:{1}, May:{2}, Jun:{1}, Jul:{2}, Aug:{2}, \
 Sep:{1}, Oct:{2}, Nov:{1}, Dec:{2}""".format(28, 30, 31))
"""
It is not mandatory to provide the replacement field numbers in the string. Replacement
will happen just fine with simple "{}". However, in such case the order of the replacement
fields cannot be changed and the replacement fields cannot be reused.
"""
print("My age is {} years".format(age))
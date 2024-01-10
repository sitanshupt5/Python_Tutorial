"""
Strings are one of python's sequence datatypes.
Meaning a string is a sequence of characters.
"""
bird = "Bald Eagle"
print(bird)
"""
It is possible to print a particular character out of a String. This is called indexing.
for example:
"""
print(bird[3])
# We can use negative integers for indexing where -1 would refer to the last character.
print(bird[-1])

"""
We can provide a range of indexes inorder to get a slice of the string. 
Slicing can be achieved by providing a ':' between the required indices.
for example:
"""
print(bird[0:5])
"""
Here the sequence of characters starting from the 1st index upto but not including the
the 5th index are printed. In case the start or end index values are not provided, then
by default the starting index of the of the string or the ending index is assumed.
for example:
"""
print(bird[:5])
print(bird[5:])
""" 
Slicing can also be done using negative indices. However, one must keep in mind that
end index cannot be lower than the start index. Meaning in above example:
print(bird[-2:-8]) will not work.
We can also use a combination of positive and negative indices at either positions.
"""
print(bird[-10:-5])
print(bird[-5:10])

# Slicing can also be done with variable steps. The default value though is 1.
print(bird[0:10:2])
print(bird[0:9:3])
"""
Incase of line 39 the syntax will slice the string from the 1st index till the 10 index
and return values in steps of 2. Hence, the output will be "Bl al"
Similarly, incase of line 40 the syntax will slice the string from the 1st index till the
9th index and return values in steps of 3. Hence, output will be "Bdg". 
"""
# Backwards slicing in python is possible using negative step value. Consider below:
alphabet = "abcdefghijklmnopqrstuvwxyz"
backwards = alphabet[25:0:-1]
print(backwards)
"""
In the above code snippet we are starting from the last index backwards with steps of 1
upto but not including the 1st index. Hence, the output will be "zyxwvutsrqponmlkjihgfedcb".
If there is a negative step then the positions of the start and end indices in the syntax
get rearranged. Hence, alphabet[25::-1] will work the to reverse the string also including
the first index. Also, alphabet[::-1] will do the same work as in the above case.
Please refer below:
"""
backwards = alphabet[::-1]
print(backwards)
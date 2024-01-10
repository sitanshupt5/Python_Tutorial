"""
Strings are the most common examples of python sequence dataTypes. Hence, most of the examples
will be wrt to String data types.
"""
# Strings can be concatenated using the '+' operator
string1 = "He's "
string2 = "probably "
string3 = "gunning "
string4 = "for the "
string5 = "top spot"

print(string1 + string2 + string3 + string4 +string5)
print("He's " "probably " "gunning " "for the " "top spot")

"""
We can also multiply strings in python using the '*' operator. The operator prints the 
said string n number of times. However in such a case operator precedence must be kept in
mind.
"""
print("Hello " * 5)
"""
However, if try the syntax print("Hello" * 5 + 4), it wont print the string 9 times.
Rather it will return error as due to operator precedence multiplication will occur first
and then concatenation will be attempted with integer 4 which will return error.
"""
print("Hello " * 5 +"4")

# We can check whether one string is the substring of another using the 'in' operator
today = "Friday"
print("day" in today)
print("Fri" in today)
print("thur" in today)
# In the above cases boolean value will be returned as the result.
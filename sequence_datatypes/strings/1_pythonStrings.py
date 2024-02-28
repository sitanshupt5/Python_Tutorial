# Strings in python can be enclosed in both double and single quotes.
# However, the strings need to be enclosed withing the same type of quotes.
# Python also allows the use of single quotes within double quotes and vice-versa. Refer below:
print("Python's strings are easy to use")
print('We can even include "double quotes" within single quotes.')
# we can even concatenate strings using the '+' operator.
print("Hello" + " World!!!")
# We can store the strings in variables. Variable declarations in python do not require data
#   type.
greetings = "Hello"
# We can also use the input() function if we want to enter the name at runtime.
name = input("Please enter your name.")
print(greetings+' '+name)

# Python also supports escape characters like \n, \t and also ways to escape delimiters.
splitString = "This string has been \nsplit over\nseveral\nlines"
print(splitString)
tabbedString = "1\t2\t3\t4\t5"
print(tabbedString)

# If we are required to use double quotes within string delimited by the same or single
# quotes within a string delimited by the single quotes then we need to use the escape
#   character.

print('The pet shop owner said "No, no, \'e\'s uh, ... he\'s resting".')
print("The pet shop owner said \"No, no, 'e's uh, ... he's resting\".")
# For the code in line 23 the String is delimited with single quotes. Hence, single quotes
#   need to be escaped. Similarly, in line 24 the same has been done for double quotes. Python
#   provides the feature of delimiting strings with 3 double quotes. The advantage of this
#   feature is strings delimited by double quotes do not require escape characters. For
#   example if we print the same string as above by delimiting with triple quotes:
print("""The pet shop owner said "No, no, 'e's uh, ... he's resting".""")

# Also we do not need to use '\n' for line breaks when using triple quotes.
anotherSplitString = """The string has been
split over
several
lines"""
print(anotherSplitString)

# The line breaks for String stored in variable anotherSplitString can be skipped if
# an escape character is placed at every line break. In such a case line breaks will show
# in the code but not in the output.

splitString2 = """The string has been \
split over \
several \
lines"""
print(splitString2)
# Backslashes in python can be escaped using to methods. Please refer below:
print("C:\\Users\\sitanshu\\tax\\notes.txt")
print(r"C:\Users\sitanshu\tax\notes.txt")
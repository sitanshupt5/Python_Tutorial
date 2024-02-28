print('Hello World!!!')
# Semi-colons (';') are not required to end the line in python as compared to java.
"""
Strings in python can be declared within (') as well as (") as compared to only double
quotes in java.
However you have to start and end with the same type of quotes. Otherwise error is 
returned. Refer below.
print('Hello World!!!")
SyntaxError: unterminated string literal (detected at line 9)
"""
# print function can accept multiple types of arguments.
print(1 + 2)  # The output of this line will be the sum of 1 and 2, i.e. 3
print(7 * 6)  # The output of this line will be the product of 7 and 6, i.e. 42
print()  # In this case a blank line will be printed in the output.
print("The end")  # This line depicts the example where strings can be printed with double quotes.

# Following example show how to print different data together using a single print function occurence.
print("Stay tuned", 'to learn more about Python', 3)
# The comma works the same way as the concat operator '+' in java. Rather it adds a space in between.
"""
The print function in python is actually much more diverse. Refer below for the signature:
print(*objects, sep=' ', end='\n', file=sys.stdout, flush=False)
Here's a breakdown of each parameter:
* objects: One or more objects to print. These are passed as separate arguments and are 
separated by the sep string. If no objects are given, only the sep string will be printed.
* sep: (Optional) A string inserted between values, default is a space ' '.
* end: (Optional) A string appended after the last value, default is a newline '\n'.
* file: (Optional) A file-like object (stream); defaults to the current sys.stdout.
* flush: (Optional) Whether to forcibly flush the stream, default is False. If True, the 
output will be written immediately.

Note: The * before objects indicates that the function accepts a variable number of 
positional arguments, allowing you to pass any number of arguments separated by commas.
"""
name = "Sitanshu"
age = 32

print(name, age, "Python", 2024)
print(name, age, "Python", 2024, sep=", ")
print(name, age, "Python", 2024, sep=", ", end="\t")

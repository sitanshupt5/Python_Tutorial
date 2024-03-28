"""
NOTE: Most of the concepts in this section will be discussed through example exercises.
Hence, Please go through all the excercise python files.

A function is a block of organised reusable code designed to perform a specific task.
The basic syntax structure of defining a function in python is as follows:

def function_name(arg1, arg2, ...)
    # function body
    return result

Following is a breakdown of the key components of the syntax:
def:                           | It is the keyword used to define a function.
function_name:                 | This is the name of the function.
arguments:                     | These are placeholders for values that you pass to the
                               | function when calling it.Functions can have zero or more
                               | parameters
function body:                 | It contains the actual code that the function executes.
                               | It is indented to distinguish it from the surrounding code.
return statement (optional):   | It is used to return a value from the function to the
                               | caller. If omitted, the function returns None by default.

Ideally, as mentioned in the python style guide a function body should be followed by 2
blank lines. This is for the code to be more readable.
Lets, take a look at different examples of function declaration and definition.
"""
# DEFINING A FUNCTION WITHOUT ANY ARGUMENTS:

str1 = "Sitanshu Pati"


def object_printer():
    print(str1)


object_printer()

"""
The above function does not take any arguments nor does it return any values. It simply
prints the value on the console.
"""

# DEFINING FUNCTIONS WITH ARGUMENTS AND RETURNS:
integer1 = 12
integer2 = 8


def addition(x, y):
    result = x + y
    return result


print(f"The addition results for {integer1} and {integer2} is: ")
print(addition(integer1, integer2))
print()


def subtraction(x, y):
    result = x - y
    return result


print(f"The subtraction results for {integer1} and {integer2} is: ")
print(subtraction(integer1, integer2))
print()


def multiplication(x, y):
    result = x * y
    return result


print(f"The multiplication results for {integer1} and {integer2} is: ")
print(multiplication(integer1, integer2))
print()


def division(x, y):
    result = x / y
    return result


print(f"The division results for {integer1} and {integer2} is: ")
print(division(integer1, integer2))
print()

"""
The functions in python by default return a value. If the value to be returned by the function
is not explicitly mentioned then the function returns the value none.
Please refer to the below example:
"""


def multiply(x, y):
    result = x * y


print(multiply(integer1, integer2))
"""
The output for line 95 will be 'None'. This is because the function does not explicitly return
the result. So intead, the default value of 'None' is returned.
"""